SHELL := /bin/bash

.SILENT:

.PHONY: help
.DEFAULT_GOAL := help
help:  ## Prints all the targets in all the Makefiles
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#######################
### Hugo Development ###
#######################

.PHONY: hugo_server
hugo_server:  ## Run Hugo server (kills any existing server first)
	@echo "Killing any existing Hugo server processes..."
	@pkill -f "hugo server" 2>/dev/null || true
	@sleep 1
	@echo "Cleaning previous Hugo build artifacts..."
	@rm -rf public resources/_gen
	@echo "Starting Hugo server on port 1313..."
	hugo server -D --port 1313

.PHONY: test_workflow
test_workflow:  ## Test GitHub workflow build locally (mirrors .github/workflows/hugo.yaml)
	@echo "=== Checking Hugo version ==="
	hugo version
	@echo ""
	@echo "=== Checking for submodules ==="
	git submodule status
	@echo ""
	@echo "=== Installing Node.js dependencies (if any) ==="
	@if [ -f package-lock.json ] || [ -f npm-shrinkwrap.json ]; then npm ci; else echo "No Node.js dependencies found"; fi
	@echo ""
	@echo "=== Building with Hugo (production environment) ==="
	HUGO_ENVIRONMENT=production HUGO_ENV=production hugo \
		--gc \
		--minify \
		--baseURL "http://www.olshansky.info/"
	@echo ""
	@echo "=== Build complete! Output in ./public ==="
	@ls -la public/ | head -10

#########################
### Content Creation  ###
#########################

.PHONY: new_thought
new_thought:  ## Create new thought post (usage: make new_thought TITLE="My Thought")
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_thought TITLE=\"My Thought\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh thought "$(TITLE)"

.PHONY: new_post
new_post:  ## Create new blog post (usage: make new_post TITLE="My Post")
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_post TITLE=\"My Post\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh post "$(TITLE)"

.PHONY: new_movie
new_movie:  ## Create new movie review (usage: make new_movie TITLE="Movie Name")
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_movie TITLE=\"Movie Name\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh movie "$(TITLE)"

.PHONY: new_tv_show
new_tv_show:  ## Create new TV show review (usage: make new_tv_show TITLE="Show Name")
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_tv_show TITLE=\"Show Name\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh tv_show "$(TITLE)"

.PHONY: new_book
new_book:  ## Create new book review (usage: make new_book TITLE="Book Name")
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_book TITLE=\"Book Name\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh book "$(TITLE)"

######################
### CV/Resume      ###
######################

.PHONY: resume_deps
resume_deps:  ## Install LaTeX dependencies (BasicTeX via Homebrew)
	@echo "=== Checking for pdflatex ==="
	@if command -v pdflatex >/dev/null 2>&1; then \
		echo "✓ pdflatex already installed at $$(which pdflatex)"; \
	else \
		echo "✗ pdflatex not found. Installing BasicTeX (~100MB download)..."; \
		echo "This may take a few minutes..."; \
		brew install --cask basictex; \
		echo ""; \
		echo "=== Installation complete! ==="; \
		echo ""; \
		echo "IMPORTANT: Update your PATH to use pdflatex"; \
		echo "Run one of the following:"; \
		echo ""; \
		echo "  # For current shell:"; \
		echo "  eval \"\$$(/usr/libexec/path_helper)\""; \
		echo ""; \
		echo "  # Or add to ~/.zshrc (permanent):"; \
		echo "  echo 'export PATH=\"/Library/TeX/texbin:\$$PATH\"' >> ~/.zshrc"; \
		echo "  source ~/.zshrc"; \
		echo ""; \
		echo "Then run: make resume_short"; \
	fi

.PHONY: resume_short
resume_short:  ## Convert cv/resume_short.tex to PDF
	@echo "=== Converting resume_short.tex to PDF ==="
	@if ! command -v pdflatex >/dev/null 2>&1; then \
		echo "Error: pdflatex not found. Run 'make resume_deps' first."; \
		exit 1; \
	fi
	@cd cv && pdflatex -interaction=nonstopmode -halt-on-error resume_short.tex > /dev/null 2>&1 || \
		(echo "Error: LaTeX compilation failed. Check cv/resume_short.log for details." && exit 1)
	@echo "=== PDF generated at cv/resume_short.pdf ==="

.PHONY: resume_clean
resume_clean:  ## Clean LaTeX auxiliary files
	@echo "=== Cleaning LaTeX auxiliary files ==="
	@rm -f cv/*.aux cv/*.log cv/*.out cv/*.toc
	@echo "Done!"

#########################
### AI Content Tools  ###
#########################

.PHONY: add_tags
add_tags:  ## Auto-generate tags for content file (usage: make add_tags FILE=content/thoughts/my-post.md)
	@if [ -z "$(FILE)" ]; then \
		echo "Error: FILE is required. Usage: make add_tags FILE=content/thoughts/my-post.md"; \
		exit 1; \
	fi
	@if [ ! -f "$(FILE)" ]; then \
		echo "Error: File '$(FILE)' not found"; \
		exit 1; \
	fi
	@echo "=== Generating tags for $(FILE) ==="
	@claude --print "Read the file $(FILE) and analyze its content. Based on the content, suggest appropriate tags and update the file's front matter tags field. Use title case for tags (e.g., 'Machine Learning' not 'machine-learning'). Keep tags concise (1-3 words each) and relevant. Aim for 3-7 tags. Only update the tags field, do not modify any other content."

#########################
### Code Maintenance  ###
#########################

.PHONY: todo
todo:  ## Grep codebase for TODO comments
	@echo "=== Searching for TODO items ==="
	@grep -rn "TODO" . \
		--exclude-dir=.git \
		--exclude-dir=node_modules \
		--exclude-dir=public \
		--exclude-dir=resources \
		--exclude-dir=vendor \
		--exclude="*.log" \
		--color=always || echo "No TODO items found"
