#!/usr/bin/env python3

import json
import csv
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

def generate_csv_report():
    """Generate CSV report for easier review."""
    # Load export data
    print("Loading export data...")
    medium_posts = load_json_file('/Users/olshansky/workspace/olshansk.github.io/medium_posts_with_images.json')
    substack_posts = load_json_file('/Users/olshansky/workspace/olshansk.github.io/substack_images_analysis.json')

    # Scan markdown files
    print("Scanning markdown files...")
    posts_dir = '/Users/olshansky/workspace/olshansk.github.io/content/posts'
    markdown_files = scan_markdown_files(posts_dir)

    # Analysis results
    results = []

    # Process Medium posts
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

    # Write CSV file
    csv_file = '/Users/olshansky/workspace/olshansk.github.io/image_comparison_report.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'source', 'export_has_images', 'export_image_count',
                     'site_has_images', 'site_image_count', 'status', 'markdown_file']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in sorted(results, key=lambda x: (x['status'], x['title'])):
            writer.writerow(result)

    print(f"CSV report saved to: {csv_file}")
    return results

if __name__ == "__main__":
    generate_csv_report()