#!/usr/bin/env python3
"""
Medium Post Migration Script
Systematically converts Medium HTML exports to Hugo markdown posts.

Quality Standards:
- Perfect content preservation
- All formatting maintained (headers, lists, code blocks)
- Images extracted and locally hosted
- Complete frontmatter generation
- Source URL attribution
"""

import os
import re
import json
import requests
import hashlib
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup
import html2text
import time

class MediumMigrator:
    def __init__(self, medium_export_path, hugo_content_path, static_images_path):
        self.medium_export_path = Path(medium_export_path)
        self.hugo_content_path = Path(hugo_content_path)
        self.static_images_path = Path(static_images_path)

        # Create directories
        self.hugo_content_path.mkdir(parents=True, exist_ok=True)
        self.static_images_path.mkdir(parents=True, exist_ok=True)

        # Configure html2text
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.ignore_emphasis = False
        self.h2t.body_width = 0  # No line wrapping
        self.h2t.unicode_snob = True
        self.h2t.mark_code = True

        # Track processed posts
        self.processed_count = 0
        self.skipped_count = 0
        self.error_count = 0

        # Get existing posts with medium_url to avoid duplicates
        self.existing_medium_posts = self._get_existing_medium_posts()

    def _get_existing_medium_posts(self):
        """Get list of already migrated Medium posts"""
        existing = set()
        posts_dir = self.hugo_content_path / "posts"

        if not posts_dir.exists():
            return existing

        for post_file in posts_dir.glob("*.md"):
            try:
                with open(post_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Extract medium_url from frontmatter
                    if 'medium_url:' in content:
                        lines = content.split('\n')
                        for line in lines:
                            if line.strip().startswith('medium_url:'):
                                url = line.split(':', 1)[1].strip().strip('"').strip("'")
                                # Extract the post ID from the URL
                                post_id = self._extract_post_id_from_url(url)
                                if post_id:
                                    existing.add(post_id)
                                break
            except Exception as e:
                print(f"Error reading {post_file}: {e}")

        print(f"Found {len(existing)} existing Medium posts")
        return existing

    def _extract_post_id_from_url(self, url):
        """Extract Medium post ID from URL"""
        if not url:
            return None
        # Medium URLs typically end with the post ID
        parts = url.rstrip('/').split('/')
        if parts and len(parts[-1]) > 10:  # Post IDs are long
            return parts[-1].split('-')[-1] if '-' in parts[-1] else parts[-1]
        return None

    def _extract_post_id_from_filename(self, filename):
        """Extract post ID from HTML filename"""
        # Format: YYYY-MM-DD_Title---ID.html
        if '--' in filename:
            return filename.split('--')[-1].replace('.html', '')
        elif filename.count('_') >= 2:
            # Sometimes format is different, extract last part after last underscore
            parts = filename.replace('.html', '').split('_')
            if len(parts) >= 2 and len(parts[-1]) > 10:
                return parts[-1]
        return None

    def parse_html_post(self, html_file):
        """Parse Medium HTML export file"""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            # Extract metadata
            title_elem = soup.find('h1', class_='p-name')
            title = title_elem.get_text().strip() if title_elem else "Untitled"

            # Extract subtitle/description
            subtitle_elem = soup.find('section', {'data-field': 'subtitle'})
            subtitle = subtitle_elem.get_text().strip() if subtitle_elem else ""

            # Extract publish date from footer
            time_elem = soup.find('time', class_='dt-published')
            if time_elem:
                date_str = time_elem.get('datetime')
                publish_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            else:
                # Fallback: extract from filename
                filename = Path(html_file).name
                date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
                if date_match:
                    publish_date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
                else:
                    publish_date = datetime.now()

            # Extract canonical URL
            canonical_elem = soup.find('a', class_='p-canonical')
            medium_url = canonical_elem.get('href') if canonical_elem else ""

            # Extract main content
            content_section = soup.find('section', {'data-field': 'body'})
            if not content_section:
                content_section = soup.find('section', class_='e-content')

            if not content_section:
                print(f"No content section found in {html_file}")
                return None

            # Clean up content section for conversion
            # Remove section dividers
            for divider in content_section.find_all('div', class_='section-divider'):
                divider.decompose()

            # Process images before conversion
            images_info = []
            for img in content_section.find_all('img'):
                img_src = img.get('data-src') or img.get('src')
                if img_src:
                    images_info.append({
                        'original_src': img_src,
                        'alt': img.get('alt', ''),
                        'element': img
                    })

            # Convert to markdown
            content_html = str(content_section)
            markdown_content = self.h2t.handle(content_html)

            # Clean up markdown
            markdown_content = self._clean_markdown(markdown_content)

            return {
                'title': title,
                'subtitle': subtitle,
                'content': markdown_content,
                'publish_date': publish_date,
                'medium_url': medium_url,
                'images': images_info,
                'html_file': html_file
            }

        except Exception as e:
            print(f"Error parsing {html_file}: {e}")
            return None

    def _clean_markdown(self, markdown):
        """Clean up converted markdown"""
        # Remove excessive newlines
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        # Fix list formatting
        markdown = re.sub(r'^\s*\d+\.\s+', lambda m: f"{m.group().strip()}\n", markdown, flags=re.MULTILINE)

        # Clean up headers
        markdown = re.sub(r'^#+\s*$', '', markdown, flags=re.MULTILINE)

        # Remove trailing whitespace
        lines = [line.rstrip() for line in markdown.split('\n')]
        markdown = '\n'.join(lines)

        return markdown.strip()

    def _download_image(self, img_url, post_slug, img_index):
        """Download image from Medium CDN"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }

            response = requests.get(img_url, headers=headers, timeout=30)
            response.raise_for_status()

            # Determine file extension
            content_type = response.headers.get('content-type', '')
            if 'png' in content_type:
                ext = 'png'
            elif 'jpeg' in content_type or 'jpg' in content_type:
                ext = 'jpg'
            elif 'gif' in content_type:
                ext = 'gif'
            elif 'webp' in content_type:
                ext = 'webp'
            else:
                # Try to extract from URL
                parsed_url = urlparse(img_url)
                path_ext = Path(parsed_url.path).suffix.lower()
                ext = path_ext[1:] if path_ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp'] else 'jpg'

            # Create filename
            filename = f"{post_slug}-image-{img_index:02d}.{ext}"
            filepath = self.static_images_path / filename

            # Save image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            # Return relative path for markdown
            return f"/images/posts/{filename}"

        except Exception as e:
            print(f"Failed to download image {img_url}: {e}")
            return None

    def _process_images(self, post_data, post_slug):
        """Process all images in a post"""
        if not post_data['images']:
            return post_data['content']

        content = post_data['content']

        for i, img_info in enumerate(post_data['images'], 1):
            img_url = img_info['original_src']

            # Download image
            local_path = self._download_image(img_url, post_slug, i)

            if local_path:
                # Replace Medium URL with local path in content
                content = content.replace(img_url, local_path)
            else:
                # Keep original URL if download failed
                print(f"Keeping original URL for failed download: {img_url}")

        return content

    def _generate_slug(self, title, date):
        """Generate URL-safe slug from title"""
        # Remove special characters, keep alphanumeric and spaces
        slug = re.sub(r'[^\w\s-]', '', title.lower())
        # Replace spaces with hyphens
        slug = re.sub(r'[\s_-]+', '-', slug)
        # Remove leading/trailing hyphens
        slug = slug.strip('-')

        # Add date prefix for uniqueness
        date_prefix = date.strftime('%Y-%m-%d')

        return f"{date_prefix}-{slug}"

    def _generate_frontmatter(self, post_data, slug):
        """Generate Hugo frontmatter"""
        title = post_data['title'].replace('"', '\\"')

        # Extract categories/tags from title and content (basic heuristics)
        content_lower = post_data['content'].lower()
        title_lower = title.lower()

        tags = []
        categories = []

        # Tech-related categories
        if any(word in content_lower or word in title_lower for word in
               ['bitcoin', 'crypto', 'blockchain', 'ethereum']):
            categories.append('cryptocurrency')

        if any(word in content_lower or word in title_lower for word in
               ['python', 'golang', 'javascript', 'programming', 'code', 'development']):
            categories.append('technology')

        if any(word in content_lower or word in title_lower for word in
               ['machine learning', 'ai', 'data science', 'model', 'algorithm']):
            categories.append('machine-learning')

        if any(word in content_lower or word in title_lower for word in
               ['startup', 'business', 'company', 'entrepreneur']):
            categories.append('business')

        # Default category
        if not categories:
            categories.append('general')

        # Generate basic tags from title words
        title_words = re.findall(r'\b\w{3,}\b', title_lower)
        common_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use'}

        for word in title_words[:3]:  # Take first 3 meaningful words
            if word not in common_words:
                tags.append(word)

        frontmatter = f"""---
title: "{title}"
date: {post_data['publish_date'].strftime('%Y-%m-%dT%H:%M:%S-07:00')}
draft: false"""

        if post_data.get('subtitle'):
            subtitle = post_data['subtitle'].replace('"', '\\"')
            frontmatter += f'\ndescription: "{subtitle}"'

        if tags:
            frontmatter += f"\ntags: {tags}"

        if categories:
            frontmatter += f"\ncategories: {categories}"

        if post_data.get('medium_url'):
            frontmatter += f'\nmedium_url: "{post_data["medium_url"]}"'

        frontmatter += """
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

"""
        return frontmatter

    def _should_skip_post(self, html_file, post_data):
        """Determine if post should be skipped"""
        filename = Path(html_file).name

        # Skip drafts
        if filename.startswith('draft_'):
            print(f"Skipping draft: {filename}")
            return True

        # Skip very short posts (likely just comments or responses)
        if len(post_data['content'].strip()) < 200:
            print(f"Skipping short post: {filename}")
            return True

        # Skip if no title
        if not post_data['title'] or post_data['title'].lower() in ['untitled', '']:
            print(f"Skipping untitled post: {filename}")
            return True

        # Check if already migrated
        if post_data.get('medium_url'):
            post_id = self._extract_post_id_from_url(post_data['medium_url'])
            if post_id in self.existing_medium_posts:
                print(f"Skipping already migrated post: {filename}")
                return True

        # Check by filename post ID
        file_post_id = self._extract_post_id_from_filename(filename)
        if file_post_id in self.existing_medium_posts:
            print(f"Skipping already migrated post by filename: {filename}")
            return True

        return False

    def migrate_post(self, html_file):
        """Migrate single Medium post"""
        try:
            print(f"\nProcessing: {Path(html_file).name}")

            # Parse HTML
            post_data = self.parse_html_post(html_file)
            if not post_data:
                self.error_count += 1
                return False

            # Check if should skip
            if self._should_skip_post(html_file, post_data):
                self.skipped_count += 1
                return False

            # Generate slug
            slug = self._generate_slug(post_data['title'], post_data['publish_date'])

            # Process images
            content_with_images = self._process_images(post_data, slug)
            post_data['content'] = content_with_images

            # Generate frontmatter
            frontmatter = self._generate_frontmatter(post_data, slug)

            # Create final markdown file
            final_content = frontmatter + post_data['content']

            # Write to file
            output_file = self.hugo_content_path / "posts" / f"{slug}.md"
            output_file.parent.mkdir(parents=True, exist_ok=True)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_content)

            print(f"✓ Migrated: {post_data['title'][:50]}...")
            self.processed_count += 1

            # Small delay to be respectful to Medium CDN
            time.sleep(0.5)

            return True

        except Exception as e:
            print(f"✗ Error processing {html_file}: {e}")
            self.error_count += 1
            return False

    def migrate_all_posts(self):
        """Migrate all Medium posts"""
        posts_dir = self.medium_export_path / "posts"

        if not posts_dir.exists():
            print(f"Posts directory not found: {posts_dir}")
            return

        html_files = list(posts_dir.glob("*.html"))
        total_files = len(html_files)

        print(f"Found {total_files} HTML files to process")
        print(f"Will skip {len(self.existing_medium_posts)} already migrated posts")

        for i, html_file in enumerate(html_files, 1):
            print(f"\n[{i}/{total_files}]", end=" ")
            self.migrate_post(html_file)

        # Print summary
        print(f"\n{'='*60}")
        print(f"MIGRATION COMPLETE")
        print(f"{'='*60}")
        print(f"Total files processed: {total_files}")
        print(f"Successfully migrated: {self.processed_count}")
        print(f"Skipped (duplicates/drafts/short): {self.skipped_count}")
        print(f"Errors: {self.error_count}")
        print(f"{'='*60}")

def main():
    """Main execution function"""
    # Paths
    medium_export_path = "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium"
    hugo_content_path = "/Users/olshansky/workspace/olshansk.github.io/content"
    static_images_path = "/Users/olshansky/workspace/olshansk.github.io/static/images/posts"

    # Create migrator and run
    migrator = MediumMigrator(medium_export_path, hugo_content_path, static_images_path)
    migrator.migrate_all_posts()

if __name__ == "__main__":
    main()