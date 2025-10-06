#!/usr/bin/env python3
"""
Script to extract image information from HTML files in the Substack posts directory.
Finds all img tags and figure elements, extracts URLs, alt text, and position information.
"""

import os
import re
from bs4 import BeautifulSoup
import json

def extract_title_from_filename(filename):
    """Extract post title from filename"""
    # Remove the number prefix and .html suffix, then clean up
    title = re.sub(r'^\d+\.', '', filename)
    title = title.replace('.html', '').replace('-', ' ').title()
    return title

def extract_images_from_html(file_path):
    """Extract image information from a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        images = []

        # Find all img tags
        img_tags = soup.find_all('img')
        for i, img in enumerate(img_tags):
            image_info = {
                'type': 'img',
                'position': i + 1,
                'src': img.get('src', ''),
                'alt': img.get('alt', ''),
                'title': img.get('title', ''),
                'width': img.get('width', ''),
                'height': img.get('height', ''),
                'data_attrs': img.get('data-attrs', ''),
            }

            # Extract caption from parent figure if exists
            figure_parent = img.find_parent('figure')
            if figure_parent:
                figcaption = figure_parent.find('figcaption')
                if figcaption:
                    image_info['caption'] = figcaption.get_text(strip=True)

            images.append(image_info)

        # Find all figure elements (might contain additional image info)
        figure_tags = soup.find_all('figure')
        for i, figure in enumerate(figure_tags):
            # Skip if we already processed this figure's img tag
            if figure.find('img'):
                continue

            # Look for other image-like content in figures
            image_links = figure.find_all('a', {'class': re.compile(r'image-link')})
            for link in image_links:
                image_info = {
                    'type': 'figure_link',
                    'position': f'figure_{i + 1}',
                    'href': link.get('href', ''),
                    'alt': '',
                    'caption': ''
                }

                figcaption = figure.find('figcaption')
                if figcaption:
                    image_info['caption'] = figcaption.get_text(strip=True)

                images.append(image_info)

        return images

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return []

def main():
    posts_dir = '/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/substack/posts/'
    results = []

    # Get all HTML files that contain images
    image_files = [
        '97948865.probability-distributions-101.html',
        '98136556.kzg-via-ecg.html',
        '96065157.chatgpt-and-schools.html',
        '96895092.grandparents-in-tech.html',
        '85758661.soaring-over-a-cliff.html',
        '88092921.24-hours-of-chatgpt.html',
        '94682437.disney-reverting-to-the-mean.html',
        '72740291.an-incentive-to-label.html',
        '79432950.the-4-week-project-checklist.html',
        '59329600.infracon-v1-6-months-in-deep-pockets.html',
        '68534915.5p1r-celestia-lazyledger-white-paper.html',
        '70172236.5p1r-jellyfish-merkle-tree.html',
        '51887479.code-reviews-come-in-all-shapes-and.html',
        '52227108.5p1r-bitcoins-elliptic-curve-cryptography.html',
        '52717070.5p1r-ethereums-modified-merkle-patricia.html',
        '44684779.a-life-changing-trip-to-mexico-on.html',
        '154207074.time-boxing-engineers.html',
        '156772748.no-revisiting-the-best-nuclear-investment.html',
        '171621778.how-a-web2-company-uses-crypto-to.html',
        '153765031.aspire-to-inspire-your-present-self.html',
        '154179411.no-rss-feed-no-problem-using-claude.html',
        '151731638.my-top-x-2024-recommendations.html',
        '151420498.gateway-abstraction.html',
        '150492795.the-power-of-analogies.html',
        '150806653.using-llms-to-save-a-geotechnical.html',
        '150911572.every-mantra-has-a-counter-mantra.html',
        '149545794.living-legends-finance-and-investing.html',
        '149931799.the-universal-api-token-a-dlt-first.html',
        '150058236.stream-of-thought-note-taking.html',
        '148353632.reflections-of-working-in-crypto.html',
        '148702489.move-fast-and-document-things.html',
        '148831220.dont-apologize-for-sending-voice.html',
        '146614143.annotated-presentation-relay-mining.html',
        '144312282.why-im-allocating-10-of-my-portfolio.html',
        '144917492.vibe-checks-are-all-you-need.html',
        '144980765.5p1r-decentralized-ai-permissionless.html',
        '141829008.no-one-wants-to-host-their-own-llm.html',
        '142497534.a-view-on-ai-agents-through-the-less.html',
        '143614317.from-pc-personal-computer-to-pgpt.html',
        '140044129.i-made-it-to-the-anti-portfolio-of.html',
        '140064883.help-a-family-create-a-memory.html',
        '140529118.til-about-the-reach-of-redditcomrtodayilearned.html',
        '138972450.why-was-sam-altman-fired-from-openai.html',
        '139312617.5p1r-stackr-micro-rollups.html',
        '140044081.use-apps-not-tabs.html',
        '137525653.why-pocket-is-rolling-with-rollkit.html',
        '138026361.creative-copay-coupons.html',
        '123181044.steering-the-future-navigating-ai.html',
        '132414630.data-odyssey-taking-control-of-my.html',
        '135754550.a-movie-and-a-book.html',
        '118416420.you-and-your-research.html'
    ]

    print(f"Processing {len(image_files)} HTML files with images...")

    for filename in image_files:
        file_path = os.path.join(posts_dir, filename)

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        print(f"Processing: {filename}")

        # Extract title from filename
        title = extract_title_from_filename(filename)

        # Extract images from the file
        images = extract_images_from_html(file_path)

        if images:
            result = {
                'filename': filename,
                'title': title,
                'image_count': len(images),
                'images': images
            }
            results.append(result)
            print(f"  Found {len(images)} images")
        else:
            print(f"  No images found")

    # Sort results by filename for consistency
    results.sort(key=lambda x: x['filename'])

    # Save results to JSON file
    output_file = '/Users/olshansky/workspace/olshansk.github.io/substack_images_analysis.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nAnalysis complete! Results saved to: {output_file}")
    print(f"Total posts with images: {len(results)}")
    print(f"Total images found: {sum(r['image_count'] for r in results)}")

    # Print summary
    print(f"\n=== SUMMARY ===")
    for result in results:
        print(f"{result['title']} ({result['filename']}): {result['image_count']} images")

if __name__ == "__main__":
    main()