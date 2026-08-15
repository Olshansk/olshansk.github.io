#!/usr/bin/env bash
#
# Generate static/llms.txt (table of contents) and static/llms-full.txt (full content)
# Usage: ./scripts/generate_llms.sh [--force]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONTENT_DIR="$ROOT_DIR/content"
STATIC_DIR="$ROOT_DIR/static"
INTRO_FILE="$ROOT_DIR/templates/llms_intro.md"
LLMS_TXT="$STATIC_DIR/llms.txt"
LLMS_FULL="$STATIC_DIR/llms-full.txt"
BASE_URL="https://olshansky.info"

FORCE=false
if [[ "${1:-}" == "--force" ]]; then
    FORCE=true
fi

# --- Freshness check ---
if [[ "$FORCE" == false && -f "$LLMS_FULL" ]]; then
    NEWER=$(find "$CONTENT_DIR" -name "*.md" -newer "$LLMS_FULL" 2>/dev/null | head -1)
    INTRO_NEWER=""
    if [[ -f "$INTRO_FILE" && "$INTRO_FILE" -nt "$LLMS_FULL" ]]; then
        INTRO_NEWER="yes"
    fi
    if [[ -z "$NEWER" && -z "$INTRO_NEWER" ]]; then
        echo "llms.txt and llms-full.txt are up to date. Use --force to regenerate."
        exit 0
    fi
fi

echo "Generating llms.txt and llms-full.txt..."

# --- Helpers ---

# Extract a field from YAML (---) or TOML (+++) frontmatter
# Usage: extract_field <file> <field>
extract_field() {
    local file="$1"
    local field="$2"
    local first_line
    first_line=$(head -1 "$file")

    if [[ "$first_line" == "---" ]]; then
        # YAML: field: "value" or field: value
        sed -n '/^---$/,/^---$/p' "$file" | grep -m1 "^${field}:" | sed 's/^[^:]*: *//; s/^"//; s/"$//' || true
    elif [[ "$first_line" == "+++" ]]; then
        # TOML: field = "value"
        sed -n '/^+++$/,/^+++$/p' "$file" | grep -m1 "^${field} *=" | sed 's/^[^=]*= *//; s/^"//; s/"$//' || true
    fi
}

# Get the body content (everything after frontmatter)
extract_body() {
    local file="$1"
    local first_line
    first_line=$(head -1 "$file")

    if [[ "$first_line" == "---" ]]; then
        # YAML: skip first --- to second ---
        awk 'BEGIN{n=0} /^---$/{n++; next} n>=2{print}' "$file"
    elif [[ "$first_line" == "+++" ]]; then
        # TOML: skip first +++ to second +++
        awk 'BEGIN{n=0} /^\+\+\+$/{n++; next} n>=2{print}' "$file"
    else
        cat "$file"
    fi
}

# Check if a file is a draft
is_draft() {
    local file="$1"
    local draft
    draft=$(extract_field "$file" "draft")
    [[ "$draft" == "true" ]]
}

# Extract YYYY-MM-DD from a date field (handles ISO formats)
normalize_date() {
    echo "$1" | grep -oE '^[0-9]{4}-[0-9]{2}-[0-9]{2}' || true
}

# Derive Hugo slug from filename
# e.g., 2025-10-05-an-open-letter-to-llms-txt.md -> 2025-10-05-an-open-letter-to-llms-txt
file_to_slug() {
    basename "$1" .md
}

# --- Collect content files ---
# Returns lines of "date\tfile" sorted reverse chronologically
collect_files() {
    local dir="$1"
    local files=()

    for f in "$dir"/*.md; do
        [[ "$(basename "$f")" == "_index.md" ]] && continue
        [[ ! -f "$f" ]] && continue

        # Handle directories (e.g., book notes with index.md)
        if [[ -d "${f%.md}" ]]; then
            continue
        fi

        is_draft "$f" && continue

        local date_raw
        date_raw=$(extract_field "$f" "date")
        local date_norm
        date_norm=$(normalize_date "$date_raw")

        echo "${date_norm}	${f}"
    done | sort -t'	' -k1 -r
}

# Also handle directory-based content (e.g., content/book/slug/index.md)
collect_files_with_dirs() {
    local dir="$1"

    # Regular .md files
    for f in "$dir"/*.md; do
        [[ "$(basename "$f")" == "_index.md" ]] && continue
        [[ ! -f "$f" ]] && continue
        is_draft "$f" && continue

        local date_raw
        date_raw=$(extract_field "$f" "date")
        local date_norm
        date_norm=$(normalize_date "$date_raw")
        local slug
        slug=$(file_to_slug "$f")

        echo "${date_norm}	${slug}	${f}"
    done

    # Directory-based content (slug/index.md)
    for d in "$dir"/*/; do
        [[ ! -d "$d" ]] && continue
        local index="$d/index.md"
        [[ ! -f "$index" ]] && continue
        is_draft "$index" && continue

        local date_raw
        date_raw=$(extract_field "$index" "date")
        local date_norm
        date_norm=$(normalize_date "$date_raw")
        local slug
        slug=$(basename "$d")

        echo "${date_norm}	${slug}	${index}"
    done
}

# --- Generate a section for both files ---
# Args: section_title url_prefix content_dir [show_rating]
generate_section() {
    local section_title="$1"
    local url_prefix="$2"
    local content_dir="$3"
    local show_rating="${4:-false}"

    local toc_lines=""
    local full_lines=""

    if [[ ! -d "$content_dir" ]]; then
        return
    fi

    local entries
    entries=$(collect_files_with_dirs "$content_dir" | sort -t'	' -k1 -r)

    if [[ -z "$entries" ]]; then
        return
    fi

    toc_lines+="## ${section_title}"$'\n\n'
    full_lines+="## ${section_title}"$'\n\n'

    while IFS=$'\t' read -r date slug filepath; do
        [[ -z "$filepath" ]] && continue
        local title
        title=$(extract_field "$filepath" "title")
        [[ -z "$title" ]] && title="$slug"

        local url="${BASE_URL}/${url_prefix}/${slug}/"

        if [[ "$show_rating" == true ]]; then
            local rating
            rating=$(extract_field "$filepath" "rating")
            if [[ -n "$rating" ]]; then
                toc_lines+="- [${title} - ${rating}](${url})"$'\n'
                full_lines+="### ${title} - ${rating}"$'\n\n'
            else
                toc_lines+="- [${title}](${url})"$'\n'
                full_lines+="### ${title}"$'\n\n'
            fi
        else
            local display_date=""
            [[ -n "$date" ]] && display_date=" (${date})"
            toc_lines+="- [${title}${display_date}](${url})"$'\n'
            full_lines+="### ${title}${display_date}"$'\n\n'
        fi

        local body
        body=$(extract_body "$filepath")
        # Trim leading blank lines
        body=$(echo "$body" | sed '/./,$!d')

        full_lines+="${body}"$'\n\n'
        full_lines+="---"$'\n\n'

    done <<< "$entries"

    # Write to temp files (used by caller)
    echo "$toc_lines" >> "$TOC_TMP"
    echo "$full_lines" >> "$FULL_TMP"
}

# --- Main ---

TOC_TMP=$(mktemp)
FULL_TMP=$(mktemp)
trap 'rm -f "$TOC_TMP" "$FULL_TMP"' EXIT

# Start both files with the intro
if [[ -f "$INTRO_FILE" ]]; then
    cat "$INTRO_FILE" > "$TOC_TMP"
    echo "" >> "$TOC_TMP"
    cat "$INTRO_FILE" > "$FULL_TMP"
    echo "" >> "$FULL_TMP"
else
    echo "Warning: $INTRO_FILE not found. Generating without intro."
    echo "# olshansky.info" > "$TOC_TMP"
    echo "" >> "$TOC_TMP"
    echo "# olshansky.info" > "$FULL_TMP"
    echo "" >> "$FULL_TMP"
fi

# Generate each section
generate_section "Posts"         "posts"    "$CONTENT_DIR/posts"    false
generate_section "Thoughts"      "thoughts" "$CONTENT_DIR/thoughts" false
generate_section "Book Reviews"  "book"     "$CONTENT_DIR/book"     true
generate_section "Movie Reviews" "movie"    "$CONTENT_DIR/movie"    true
generate_section "TV Show Reviews" "tv"     "$CONTENT_DIR/tv"       true

# Write final files
cp "$TOC_TMP" "$LLMS_TXT"
cp "$FULL_TMP" "$LLMS_FULL"

# Stats
TOC_LINES=$(wc -l < "$LLMS_TXT" | tr -d ' ')
FULL_LINES=$(wc -l < "$LLMS_FULL" | tr -d ' ')
echo "Generated static/llms.txt (${TOC_LINES} lines)"
echo "Generated static/llms-full.txt (${FULL_LINES} lines)"
