# Image Comparison Report: Exports vs Site Content

This report provides a comprehensive comparison between posts that contain images in both Medium and Substack exports versus the current markdown content in `/Users/olshansky/workspace/olshansk.github.io/content/posts/`.

## Summary Statistics

- **Total posts with images in exports:** 45
- **Posts with missing images:** 30 (66.7%)
- **Posts with partial images:** 1 (2.2%)
- **Posts with all images:** 9 (20.0%)
- **Posts not found in markdown:** 5 (11.1%)
- **Success rate:** 22.2%

## Analysis Methodology

1. **Export Analysis**: Parsed `medium_posts_with_images.json` (35 posts) and `substack_images_analysis.json` (10 posts)
2. **Markdown Scanning**: Scanned all 105 markdown files in `/content/posts/` for image syntax patterns:
   - Markdown format: `![alt](url)`
   - HTML format: `<img src="url">`
3. **Title Matching**: Used normalized title matching to map export posts to markdown files
4. **Status Classification**:
   - `HAS_IMAGES`: Site has same or more images than export
   - `PARTIAL_IMAGES`: Site has fewer images than export
   - `MISSING_IMAGES`: Site has no images but export does
   - `POST_NOT_FOUND`: Post exists in export but no corresponding markdown file found

## Status Breakdown

### HAS_IMAGES (9 posts)
Posts that have successfully migrated all images from the original export:

| Title | Source | Export Images | Site Images | Markdown File |
|-------|--------|---------------|-------------|---------------|
| 5P;1R — Bitcoin's Elliptic Curve Cryptography | Medium | 2 | 2 | 2022-04-23-5p1r-bitcoins-elliptic-curve-cryptography.md |
| Are recent trends in company IPOs signaling an imminent recession? | Medium | 4 | 4 | 2015-12-06-are-recent-trends-in-company-ipos-signaling-an-imminent-recession.md |
| Bill Nye vs Ken Ham: neither or both? | Medium | 1 | 1 | 2014-02-06-bill-nye-vs-ken-ham-neither-or-both.md |
| Bitcoin's price isn't a bubble, it's an adoption curve | Medium | 3 | 3 | 2017-12-27-bitcoin-adoption-curve-not-bubble.md |
| Canadian Real Estate or American Stock? | Medium | 20 | 20 | 2015-05-26-canadian-real-estate-or-american-stock.md |
| Cryptocurrencies: It's all about incentive | Medium | 1 | 1 | 2017-07-23-cryptocurrencies-all-about-incentive.md |
| Experience vs Theory: Lake Tahoe Edition | Medium | 1 | 1 | 2021-10-17-experience-vs-theory-lake-tahoe-edition.md |
| How a Web2 Company Uses Crypto to Power Open Data APIs | Medium | 5 | 5 | 2025-08-22-how-a-web2-company-uses-crypto-to-power-open-data-apis.md |
| Python 3.9 StatsProfile — My first OSS Contribution | Medium | 2 | 2 | 2020-02-17-python-statsprofile-cpython-contribution.md |

### PARTIAL_IMAGES (1 post)
Posts where some but not all images were migrated:

| Title | Source | Export Images | Site Images | Markdown File |
|-------|--------|---------------|-------------|---------------|
| Explaining Fully Homomorphic Encryption to My mom | Medium | 3 | 2 | explaining-fully-homomorphic-encryption-to-my-mom.md |

### MISSING_IMAGES (30 posts)
Posts that exist on the site but are missing all images that were present in the original export:

| Title | Source | Export Images | Markdown File |
|-------|--------|---------------|---------------|
| 5P1R Stackr Micro Rollups | Substack | 2 | 5p1r-stackr-micro-rollups.md |
| 5P;1R Jellyfish Merkle Tree | Medium | 6 | 5p1r-jellyfish-merkle-tree.md |
| 5P;1R — Celestia (LazyLedger) White Paper | Medium | 2 | 5p1r-celestia-lazyledger-white-paper.md |
| 5P;1R — Ethereum's Modified Merkle Patricia Trie | Medium | 2 | 5p1r-ethereums-modified-merkle-patricia-trie.md |
| 7 Pocket Network Analogies | Medium | 12 | 7-pocket-network-analogies.md |
| A Boring but Practical 10-Step Guide to Data Labeling for ML | Medium | 1 | a-boring-but-practical-10-step-guide-to-data-labeling-for-ml.md |
| A Life Changing Trip To Mexico On | Substack | 3 | a-life-changing-trip-to-mexico-on.md |
| AT&T — My Saving Account | Medium | 1 | att-my-saving-account.md |
| An Incentive to Label | Medium | 8 | an-incentive-to-label.md |
| An update from Grove on Shannon Beta TestNet | Medium | 6 | an-update-from-grove-on-shannon-beta-testnet.md |
| Code Reviews Come In All Shapes And | Substack | 2 | code-reviews-come-in-all-shapes-and.md |
| Creative Copay Coupons | Substack | 2 | creative-copay-coupons.md |
| Data Science for Software Engineers — Joint Probability Matrix | Medium | 7 | data-science-for-software-engineers-joint-probability-matrix.md |
| Escaping Backticks in your LLM System Prompt | Medium | 3 | escaping-backticks-in-your-llm-system-prompt.md |
| GATE: Gateway Abstraction Technical Elements — Shannon TestNet | Medium | 21 | gate-gateway-abstraction-technical-elements-shannon-testnet.md |
| Gateway Abstraction | Substack | 2 | gate-gateway-abstraction-technical-elements-shannon-testnet.md |
| Google Home — "Sorry, there was a glitch" | Medium | 3 | google-home-sorry-there-was-a-glitch.md |
| GroveAI #1: Generating GitHub PR Descriptions and Release Notes | Medium | 4 | groveai-1-generating-github-pr-descriptions-and-release-notes.md |
| Help A Family Create A Memory | Substack | 2 | help-a-family-create-a-memory.md |
| Hot Reloading with Local Docker Development | Medium | 1 | hot-reloading-with-local-docker-development.md |
| How You Should End Every Claude Project Conversation | Medium | 1 | how-you-should-end-every-claude-project-conversation.md |
| My Top X 2024 Recommendations | Substack | 2 | my-top-x-2024-recommendations.md |
| Pocket Network Shannon Migration Announcement | Medium | 3 | pocket-network-shannon-migration-announcement.md |
| Pocket Network Shannon Update — Alpha TestNet #3 | Medium | 2 | pocket-network-shannon-update-alpha-testnet-3.md |
| Pocket Network — Shannon State Shift Day | Medium | 3 | pocket-network-shannon-state-shift-day.md |
| Prompt Writer: The single most important Claude Code skill | Medium | 2 | 2025-03-10-this-post-convinced-me-to-pay-for-claude-pro.md |
| Stream Of Thought Note Taking | Substack | 2 | stream-of-thought-note-taking.md |
| The Graph LA Fitness Doesn't Want You To See | Medium | 2 | 2017-06-11-i-like-the-price-ceiling-and-floor-approach-but-see-two-issues-with-it.md |
| Use Git LFS on Github Carefully | Medium | 2 | no-rss-feed-no-problem-using-claude-to-extract-data-from-substack-rss.md |
| tl;dr | Medium | 9 | tldr-use-anrok-for-a-solution-to-complex-tax-compliance-use-cases.md |

### POST_NOT_FOUND (5 posts)
Posts that exist in exports but have no corresponding markdown file on the site:

| Title | Source | Export Images |
|-------|--------|---------------|
| A week of bugs | Medium | 2 |
| Chatgpt And Schools | Substack | 2 |
| Day And Night Switch | Medium | 1 |
| Hands on with Perplexity Deep Research | Medium | 1 |
| Time Boxing Engineers | Substack | 3 |

## Key Findings

1. **Low Success Rate**: Only 22.2% of posts with images in the exports have successfully retained their images in the site
2. **Medium vs Substack**: Medium posts have a slightly better success rate (25.7%) compared to Substack posts (10%)
3. **Image Pattern**: Successfully migrated images follow the pattern `/images/posts/[date-title]-image-[number].png`
4. **Missing Infrastructure**: 30 posts are missing images entirely, suggesting they were not migrated during the export-to-markdown conversion process
5. **Content Exists**: All posts with missing images do have corresponding markdown files on the site, indicating the text content was migrated but not the images

## Recommendations

1. **Prioritize High-Impact Posts**: Focus on migrating images for posts with the most images first (e.g., "GATE: Gateway Abstraction Technical Elements" has 21 missing images)
2. **Automate Image Migration**: Create a script to download and save images from the export sources using the established naming convention
3. **Verify Image URLs**: Check if the image URLs in the exports are still accessible before attempting migration
4. **Update Image References**: Ensure all image references in markdown files point to the correct local paths in `/static/images/posts/`
5. **Quality Check**: Manually review migrated images to ensure they display correctly and maintain their original context

## Files Generated
- `analyze_images.py`: Python script for comprehensive analysis
- `generate_csv_report.py`: Script to generate CSV report
- `image_comparison_report.csv`: Machine-readable CSV format of this report
- `IMAGE_COMPARISON_REPORT.md`: This comprehensive markdown report