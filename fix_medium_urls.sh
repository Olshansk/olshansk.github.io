#!/bin/bash

# Fix Medium post migration issues by adding URLs to posts that don't have them

echo "🔧 Starting Medium URL extraction and post fixes..."

POSTS_DIR="/Users/olshansky/workspace/olshansk.github.io/content/posts"
MEDIUM_EXPORTS_DIR="/Users/olshansky/workspace/olshansk.github.io/exports_2025_09_13/medium/posts"

# Count posts without medium_url
posts_without_url=$(grep -L "medium_url:" "$POSTS_DIR"/*.md | wc -l | tr -d ' ')
echo "📊 Found $posts_without_url posts without Medium URLs"

# Process HTML files to extract URLs and titles
for html_file in "$MEDIUM_EXPORTS_DIR"/*.html; do
    if [[ "$html_file" =~ draft_ ]]; then
        continue  # Skip draft files
    fi

    # Extract canonical URL from HTML
    canonical_url=$(grep -o 'https://medium\.com/@[^"]*' "$html_file" | grep "p-canonical" -A1 | head -1)
    if [ -z "$canonical_url" ]; then
        canonical_url=$(grep -o 'https://medium\.com/@[^"]*' "$html_file" | head -1)
    fi

    # Extract title from HTML
    html_title=$(grep -o '<title>[^<]*</title>' "$html_file" | sed 's/<title>\(.*\)<\/title>/\1/' | sed 's/&amp;/\&/g')

    if [ ! -z "$canonical_url" ] && [ ! -z "$html_title" ]; then
        # Find matching markdown file by title similarity
        for md_file in "$POSTS_DIR"/*.md; do
            md_title=$(grep "^title:" "$md_file" | sed 's/title: "\(.*\)"/\1/')

            # Simple title matching (you might want to make this more sophisticated)
            if [[ "$html_title" == *"$md_title"* ]] || [[ "$md_title" == *"$html_title"* ]]; then
                # Check if already has medium_url
                if ! grep -q "medium_url:" "$md_file"; then
                    echo "🔗 Adding URL to: $(basename "$md_file")"
                    echo "   URL: $canonical_url"

                    # Add medium_url and ShowToc to frontmatter
                    sed -i '' '/^tags:/a\
medium_url: "'$canonical_url'"\
ShowToc: true\
' "$md_file"

                    # Fix header levels (convert ### to ##)
                    sed -i '' 's/^### /## /g' "$md_file"

                fi
                break
            fi
        done
    fi
done

echo "✅ Medium URL extraction completed"
echo "📋 Next steps: Remove inline ToCs and test Hugo build"