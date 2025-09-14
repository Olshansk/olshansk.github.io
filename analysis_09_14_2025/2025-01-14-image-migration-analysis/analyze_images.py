#!/usr/bin/env python3

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

def load_json_file(filepath: str) -> List[Dict]:
    """Load and parse JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return []

def extract_images_from_markdown(content: str) -> List[str]:
    """Extract image markdown syntax from content."""
    # Pattern for ![alt](url) format
    img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    # Pattern for <img> tags
    img_tag_pattern = r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>'

    images = []

    # Find markdown format images
    for match in re.finditer(img_pattern, content):
        images.append({
            'type': 'markdown',
            'alt': match.group(1),
            'url': match.group(2),
            'full_match': match.group(0)
        })

    # Find HTML img tags
    for match in re.finditer(img_tag_pattern, content, re.IGNORECASE):
        images.append({
            'type': 'html',
            'url': match.group(1),
            'full_match': match.group(0)
        })

    return images

def scan_markdown_files(posts_dir: str) -> Dict[str, Dict]:
    """Scan all markdown files for image content."""
    posts_dir_path = Path(posts_dir)
    markdown_files = {}

    for md_file in posts_dir_path.glob('*.md'):
        if md_file.name == '_index.md':
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            images = extract_images_from_markdown(content)
            markdown_files[md_file.name] = {
                'filepath': str(md_file),
                'image_count': len(images),
                'images': images,
                'content_length': len(content)
            }
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    return markdown_files

def normalize_title(title: str) -> str:
    """Normalize title for matching."""
    # Remove special characters, convert to lowercase, replace spaces with hyphens
    normalized = re.sub(r'[^\w\s-]', '', title.lower())
    normalized = re.sub(r'\s+', '-', normalized.strip())
    return normalized

def find_matching_markdown(export_title: str, export_filename: str, markdown_files: Dict) -> Optional[str]:
    """Find the matching markdown file for an export post."""
    normalized_export_title = normalize_title(export_title)

    # First try exact title match in filename
    for md_filename in markdown_files.keys():
        if normalized_export_title in md_filename:
            return md_filename

    # Try partial matches
    export_words = normalized_export_title.split('-')
    best_match = None
    best_score = 0

    for md_filename in markdown_files.keys():
        score = 0
        for word in export_words:
            if len(word) > 2 and word in md_filename:  # Only count meaningful words
                score += 1

        if score > best_score and score >= 2:  # At least 2 words match
            best_score = score
            best_match = md_filename

    return best_match

def analyze_comparison():
    """Main analysis function."""
    # Load export data
    print("Loading export data...")
    medium_posts = load_json_file('/Users/olshansky/workspace/olshansk.github.io/medium_posts_with_images.json')
    substack_posts = load_json_file('/Users/olshansky/workspace/olshansk.github.io/substack_images_analysis.json')

    # Scan markdown files
    print("Scanning markdown files...")
    posts_dir = '/Users/olshansky/workspace/olshansk.github.io/content/posts'
    markdown_files = scan_markdown_files(posts_dir)

    print(f"Found {len(medium_posts)} Medium posts with images")
    print(f"Found {len(substack_posts)} Substack posts with images")
    print(f"Found {len(markdown_files)} markdown files")

    # Analysis results
    results = []

    # Process Medium posts
    print("\nProcessing Medium posts...")
    for post in medium_posts:
        title = post.get('html_title', '')
        filename = post.get('filename', '')
        image_count = post.get('image_count', 0)

        matching_md = find_matching_markdown(title, filename, markdown_files)

        if matching_md:
            md_data = markdown_files[matching_md]
            site_image_count = md_data['image_count']

            if site_image_count == 0:
                status = 'MISSING_IMAGES'
            elif site_image_count < image_count:
                status = 'PARTIAL_IMAGES'
            else:
                status = 'HAS_IMAGES'
        else:
            matching_md = 'NOT_FOUND'
            site_image_count = 0
            status = 'POST_NOT_FOUND'

        results.append({
            'title': title,
            'source': 'Medium',
            'export_has_images': 'YES',
            'export_image_count': image_count,
            'markdown_file': matching_md,
            'site_has_images': 'YES' if (matching_md != 'NOT_FOUND' and markdown_files.get(matching_md, {}).get('image_count', 0) > 0) else 'NO',
            'site_image_count': site_image_count if matching_md != 'NOT_FOUND' else 0,
            'status': status
        })

    # Process Substack posts
    print("Processing Substack posts...")
    for post in substack_posts:
        title = post.get('title', '')
        filename = post.get('filename', '')
        image_count = post.get('image_count', 0)

        matching_md = find_matching_markdown(title, filename, markdown_files)

        if matching_md:
            md_data = markdown_files[matching_md]
            site_image_count = md_data['image_count']

            if site_image_count == 0:
                status = 'MISSING_IMAGES'
            elif site_image_count < image_count:
                status = 'PARTIAL_IMAGES'
            else:
                status = 'HAS_IMAGES'
        else:
            matching_md = 'NOT_FOUND'
            site_image_count = 0
            status = 'POST_NOT_FOUND'

        results.append({
            'title': title,
            'source': 'Substack',
            'export_has_images': 'YES',
            'export_image_count': image_count,
            'markdown_file': matching_md,
            'site_has_images': 'YES' if (matching_md != 'NOT_FOUND' and markdown_files.get(matching_md, {}).get('image_count', 0) > 0) else 'NO',
            'site_image_count': site_image_count if matching_md != 'NOT_FOUND' else 0,
            'status': status
        })

    # Generate report
    print("\n" + "="*100)
    print("IMAGE COMPARISON REPORT")
    print("="*100)

    print(f"\n{'TITLE':<50} {'SOURCE':<10} {'EXPORT':<6} {'SITE':<4} {'IMAGES (E/S)':<12} {'STATUS':<15} {'MARKDOWN FILE'}")
    print("-" * 140)

    for result in sorted(results, key=lambda x: (x['status'], x['title'])):
        title_short = result['title'][:47] + "..." if len(result['title']) > 50 else result['title']
        markdown_file = result['markdown_file'] if result['markdown_file'] != 'NOT_FOUND' else 'NOT_FOUND'
        markdown_short = markdown_file[:30] + "..." if len(markdown_file) > 33 else markdown_file

        image_ratio = f"{result['export_image_count']}/{result['site_image_count']}"

        print(f"{title_short:<50} {result['source']:<10} {result['export_has_images']:<6} {result['site_has_images']:<4} {image_ratio:<12} {result['status']:<15} {markdown_short}")

    # Summary statistics
    print("\n" + "="*100)
    print("SUMMARY STATISTICS")
    print("="*100)

    total_posts = len(results)
    missing_images = len([r for r in results if r['status'] == 'MISSING_IMAGES'])
    partial_images = len([r for r in results if r['status'] == 'PARTIAL_IMAGES'])
    has_images = len([r for r in results if r['status'] == 'HAS_IMAGES'])
    not_found = len([r for r in results if r['status'] == 'POST_NOT_FOUND'])

    print(f"Total posts with images in exports: {total_posts}")
    print(f"Posts with missing images: {missing_images}")
    print(f"Posts with partial images: {partial_images}")
    print(f"Posts with all images: {has_images}")
    print(f"Posts not found in markdown: {not_found}")
    print(f"Success rate: {((has_images + partial_images) / total_posts * 100):.1f}%")

    # Detailed breakdown by status
    print("\nDETAILED BREAKDOWN:")
    for status in ['MISSING_IMAGES', 'PARTIAL_IMAGES', 'HAS_IMAGES', 'POST_NOT_FOUND']:
        posts_with_status = [r for r in results if r['status'] == status]
        print(f"\n{status} ({len(posts_with_status)} posts):")
        for post in posts_with_status[:5]:  # Show first 5 of each category
            print(f"  - {post['title'][:60]} ({post['source']})")
        if len(posts_with_status) > 5:
            print(f"  ... and {len(posts_with_status) - 5} more")

if __name__ == "__main__":
    analyze_comparison()