#!/bin/bash

# Script to create new content files with proper templates
# Usage: ./scripts/create_content.sh <content_type> <title>

set -e

CONTENT_TYPE="$1"
TITLE="$2"

if [ -z "$CONTENT_TYPE" ] || [ -z "$TITLE" ]; then
    echo "Usage: $0 <content_type> <title>"
    echo "Content types: thought, post, movie, tv_show, book"
    exit 1
fi

# Get current date in ISO format
CURRENT_DATE=$(date +%Y-%m-%dT%H:%M:%S%z)
DATE_PREFIX=$(date +%Y-%m-%d)

# Sanitize title for filename: lowercase, replace spaces and special chars with hyphens
SANITIZED_TITLE=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')

# Set content directory and template based on type
case "$CONTENT_TYPE" in
    "thought")
        CONTENT_DIR="content/thoughts"
        TEMPLATE="templates/thought.md"
        ;;
    "post")
        CONTENT_DIR="content/posts"
        TEMPLATE="templates/post.md"
        ;;
    "movie")
        CONTENT_DIR="content/movie"
        TEMPLATE="templates/movie.md"
        ;;
    "tv_show")
        CONTENT_DIR="content/tv"
        TEMPLATE="templates/tv_show.md"
        ;;
    "book")
        CONTENT_DIR="content/book"
        TEMPLATE="templates/book.md"
        ;;
    *)
        echo "Error: Unknown content type '$CONTENT_TYPE'"
        echo "Valid types: thought, post, movie, tv_show, book"
        exit 1
        ;;
esac

# Create output filename
OUTPUT_FILE="$CONTENT_DIR/${DATE_PREFIX}-${SANITIZED_TITLE}.md"

# Check if template exists
if [ ! -f "$TEMPLATE" ]; then
    echo "Error: Template not found: $TEMPLATE"
    exit 1
fi

# Check if output file already exists
if [ -f "$OUTPUT_FILE" ]; then
    echo "Error: File already exists: $OUTPUT_FILE"
    exit 1
fi

# Create content directory if it doesn't exist
mkdir -p "$CONTENT_DIR"

# Copy template and replace placeholders
sed "s/{{DATE}}/$CURRENT_DATE/g; s/{{TITLE}}/$TITLE/g; s/{{DESCRIPTION}}//g" "$TEMPLATE" > "$OUTPUT_FILE"

echo "Created: $OUTPUT_FILE"
echo "Title: $TITLE"
echo "Date: $CURRENT_DATE"