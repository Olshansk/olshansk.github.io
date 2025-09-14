#!/usr/bin/env python3
"""
Simple script to analyze HTML files for images without external dependencies.
"""

import os
import re
import json

def extract_title_from_filename(filename):
    """Extract a readable title from the filename."""
    # Remove the date prefix and .html suffix
    title_part = re.sub(r'^\d{4}-\d{2}-\d{2}_', '', filename)
    title_part = re.sub(r'\.html$', '', title_part)
    # Replace dashes/underscores with spaces and clean up
    title = title_part.replace('-', ' ').replace('_', ' ')
    # Clean up multiple spaces
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def extract_images_from_html(content):
    """Extract image information from HTML content using regex."""
    images = []

    # Pattern to match img tags
    img_pattern = r'<img[^>]*>'
    img_matches = re.findall(img_pattern, content, re.IGNORECASE | re.DOTALL)

    for img_tag in img_matches:
        # Extract src
        src_match = re.search(r'src=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
        src = src_match.group(1) if src_match else ''

        # Extract alt
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
        alt = alt_match.group(1) if alt_match else ''

        # Extract title
        title_match = re.search(r'title=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
        title = title_match.group(1) if title_match else ''

        images.append({
            'src': src,
            'alt': alt,
            'title': title,
            'caption': '',
            'tag': img_tag.strip()[:100] + ('...' if len(img_tag.strip()) > 100 else '')
        })

    return images

def extract_title_from_html(content):
    """Extract title from HTML content."""
    # Try to find title tag
    title_match = re.search(r'<title[^>]*>([^<]*)</title>', content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        # Clean up common Medium title suffixes
        title = re.sub(r'\s*\|\s*by\s+.*$', '', title)
        title = re.sub(r'\s*\|\s+Medium$', '', title)
        return title

    # Try to find h1
    h1_match = re.search(r'<h1[^>]*>([^<]*)</h1>', content, re.IGNORECASE | re.DOTALL)
    if h1_match:
        return h1_match.group(1).strip()

    return None

def estimate_position(content, img_tag):
    """Estimate position of image in content."""
    # Find position of image tag in content
    img_pos = content.find(img_tag)
    if img_pos == -1:
        return "Unknown"

    total_length = len(content)
    position_ratio = img_pos / total_length

    if position_ratio < 0.25:
        return "Beginning"
    elif position_ratio < 0.75:
        return "Middle"
    else:
        return "End"

def analyze_html_file(filepath):
    """Analyze a single HTML file for images."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        images = extract_images_from_html(content)

        if not images:
            return None

        filename = os.path.basename(filepath)
        html_title = extract_title_from_html(content)
        filename_title = extract_title_from_filename(filename)

        # Add position information to each image
        for img in images:
            img['position'] = estimate_position(content, img['tag'])

            # Look for figure captions near the image
            img_index = content.find(img['tag'])
            if img_index != -1:
                # Look for figcaption within 500 characters before or after
                context_start = max(0, img_index - 500)
                context_end = min(len(content), img_index + 500)
                context = content[context_start:context_end]

                figcaption_match = re.search(r'<figcaption[^>]*>([^<]*)</figcaption>', context, re.IGNORECASE)
                img['caption'] = figcaption_match.group(1).strip() if figcaption_match else ''

        return {
            'filename': filename,
            'filepath': filepath,
            'html_title': html_title,
            'filename_title': filename_title,
            'image_count': len(images),
            'images': images
        }

    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")
        return None

def main():
    # List of files that contain images (from previous grep)
    files_with_images = [
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-03-03_A-Boring-but-Practical-10-Step-Guide-to-Data-Labeling---Evaluation-47f75828fd16.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_tl-dr-4cbb7f214bd9.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2024-10-22_7-Pocket-Network-Analogies-14aecd8086ed.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2024-08-16_Pocket-Network-Shannon-Update---Alpha-TestNet--3-eca539a9e111.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-02-03_An-update-from-Grove-on-Shannon-Beta-TestNet--PATH--the-Past---the-Future-5bf7ec2a9acf.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2020-05-25_Data-Science-for-Software-Engineers---Joint-Probability-Matrices-f4fcb94d1483.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2017-07-23_Cryptocurrencies--It-s-all-about-incentive-77ac47a6adc4.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-05-06_Pocket-Network-Shannon-Migration-Announcement-139c25e4166c.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_Hands-on-with-Perplexity-Deep-Research-62753c777179.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_A-week-of-bugs-c1c45f8be035.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2022-12-26_Google-Home----Sorry--there-was-a-glitch--7e77245692f7.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-02-24_GroveAI--1--Generating-GitHub-PR-Descriptions-as-a-Team-9566273a7a80.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-05-19_Pocket-Network---Shannon-State-Shift-Day-b8c06122cb76.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2020-02-17_Python-3-9-StatsProfile---My-first-OSS-Contribution-to-cPython-9dd6847eb802.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_Use-Git-LFS-on-Github-Carefully-caa059bf7915.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_The-Graph-LA-Fitness-Doesn-t-Want-You-To-See-835914835077.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-03-04_How-You-Should-End-Every-Claude-Project-Conversation-0a88c744ef0d.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_An-Incentive-to-Label-b65cfebb8329.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2022-09-15_5P-1R-Jellyfish-Merkle-Tree-d2d7dc7dfa8e.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2014-02-06_Bill-Nye-vs-Ken-Ham--neither-or-both--9bf63f7f7d7.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_Day-And-Night-Switch-4933605686f7.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2022-04-23_5P-1R---Ethereum-s-Modified-Merkle-Patricia-Trie-6956f5888398.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2021-02-20_AT-T---My-Saving-Account-3eb035299098.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2022-08-13_5P-1R---Celestia--LazyLedger--White-Paper-9915e83a079b.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2015-05-26_Canadian-Real-Estate-or-American-Stock--6cc59f750e43.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-05-06_Escaping-Backticks-in-your-LLM-System-Prompt-6507a25b7bc8.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-08-22_How-a-Web2-Company-Uses-Crypto-to-Power-Open-Data-APIs-b8307eba173a.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2015-12-06_Are-recent-trends-in-company-IPOs-signaling-an-imminent-recession--7366d99a3246.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/draft_Prompt-Writer--The-single-most-important-Claude-Code-agent-you-ll-have--1c03c8810b36.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2017-12-27_Bitcoin-s-price-isn-t-a-bubble--it-s-an-adoption-curve-f52695df2b01.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2022-04-23_5P-1R---Bitcoin-s-Elliptic-Curve-Cryptography-196fc74a1bf1.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-08-26_Explaining-Fully-Homomorphic-Encryption-to-My-mom-c14ebb724910.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2021-10-17_Experience-vs-Theory--Lake-Tahoe-Edition-6be9216e2f57.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2020-07-19_Hot-Reloading-with-Local-Docker-Development-1ec5dbaa4a65.html",
        "/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts/2025-03-08_GATE--Gateway-Abstraction-Technical-Elements---Annotated-Presentation-2c1ee2e27373.html"
    ]

    print(f"Analyzing {len(files_with_images)} HTML files with images...")

    posts_with_images = []
    total_images = 0

    for i, filepath in enumerate(files_with_images, 1):
        print(f"Processing {i}/{len(files_with_images)}: {os.path.basename(filepath)}")

        result = analyze_html_file(filepath)
        if result:
            posts_with_images.append(result)
            total_images += result['image_count']
        else:
            print(f"  ⚠️ No images found or error processing")

    # Sort by filename for consistent output
    posts_with_images.sort(key=lambda x: x['filename'])

    print(f"\n{'='*60}")
    print(f"ANALYSIS COMPLETE")
    print(f"{'='*60}")
    print(f"Posts with images: {len(posts_with_images)}")
    print(f"Total images found: {total_images}")
    print(f"\n{'='*60}")
    print(f"DETAILED RESULTS")
    print(f"{'='*60}\n")

    for post in posts_with_images:
        print(f"📄 FILE: {post['filename']}")

        # Show title
        if post['html_title']:
            print(f"   📰 TITLE: {post['html_title']}")
        else:
            print(f"   📰 TITLE (from filename): {post['filename_title']}")

        print(f"   🖼️  IMAGES: {post['image_count']}")

        # Show each image
        for i, img in enumerate(post['images'], 1):
            print(f"   Image {i}:")
            if img['src']:
                print(f"     • URL: {img['src']}")
            if img['alt']:
                print(f"     • Alt text: {img['alt']}")
            if img['caption']:
                print(f"     • Caption: {img['caption']}")
            if img['title']:
                print(f"     • Title attr: {img['title']}")
            print(f"     • Position: {img['position']}")
        print()

    # Save to JSON
    output_file = "/Users/olshansky/workspace/olshansk.github.io/medium_posts_with_images.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(posts_with_images, f, indent=2, ensure_ascii=False)

    print(f"📁 Detailed results saved to: {output_file}")

if __name__ == "__main__":
    main()