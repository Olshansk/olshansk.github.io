SHELL := /bin/bash

.SILENT:

.PHONY: help
.DEFAULT_GOAL := help
help:
	@printf "\n"
	@printf "\033[36m╔═══════════════════════════════════╗\033[0m\n"
	@printf "\033[36m║      olshansky.info Blog          ║\033[0m\n"
	@printf "\033[36m╚═══════════════════════════════════╝\033[0m\n"
	@printf "\n"
	@printf "\033[1m=== 🚀 Hugo ===\033[0m\n"
	@printf "  \033[36mhugo_server\033[0m        Start local dev server on port 1313\n"
	@printf "  \033[36mtest_workflow\033[0m      Test GitHub Actions build locally\n"
	@printf "\n"
	@printf "\033[1m=== 📝 Content ===\033[0m\n"
	@printf "  \033[36mnew_thought\033[0m        Create thought post\n"
	@printf "                     make new_thought TITLE=\"...\"\n"
	@printf "  \033[36mnew_post\033[0m           Create blog post\n"
	@printf "                     make new_post TITLE=\"...\"\n"
	@printf "  \033[36mnew_book\033[0m           Create book review\n"
	@printf "  \033[36mnew_movie\033[0m          Create movie review\n"
	@printf "  \033[36mnew_tv_show\033[0m        Create TV show review\n"
	@printf "  \033[36madd_tags\033[0m           Auto-generate tags for content file\n"
	@printf "                     make add_tags FILE=\"content/thoughts/my-post.md\"\n"
	@printf "\n"
	@printf "\033[1m=== 📄 Resume ===\033[0m\n"
	@printf "  \033[36mresume_generate\033[0m    Generate cv/resume.pdf from LaTeX\n"
	@printf "  \033[36mresume_clean\033[0m       Remove LaTeX auxiliary files\n"
	@printf "  \033[36mresume_deps\033[0m        Install LaTeX dependencies (BasicTeX)\n"
	@printf "\n"
	@printf "\033[1m=== 🛠️  Maintenance ===\033[0m\n"
	@printf "  \033[36mtodo\033[0m               Find all TODO comments in codebase\n"
	@printf "\n"

#################
# Hugo
#################

.PHONY: hugo_server
hugo_server:
	@echo "Killing any existing Hugo server processes..."
	@pkill -f "hugo server" 2>/dev/null || true
	@sleep 1
	@echo "Cleaning previous Hugo build artifacts..."
	@rm -rf public resources/_gen
	@echo "Starting Hugo server on port 1313..."
	hugo server -D --buildFuture --port 1313

.PHONY: test_workflow
test_workflow:
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

#################
# Content
#################

.PHONY: new_thought
new_thought:
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_thought TITLE=\"My Thought\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh thought "$(TITLE)"

.PHONY: new_post
new_post:
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_post TITLE=\"My Post\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh post "$(TITLE)"

.PHONY: new_movie
new_movie:
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_movie TITLE=\"Movie Name\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh movie "$(TITLE)"

.PHONY: new_tv_show
new_tv_show:
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_tv_show TITLE=\"Show Name\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh tv_show "$(TITLE)"

.PHONY: new_book
new_book:
	@if [ -z "$(TITLE)" ]; then \
		echo "Error: TITLE is required. Usage: make new_book TITLE=\"Book Name\""; \
		exit 1; \
	fi
	@./scripts/create_content.sh book "$(TITLE)"

.PHONY: add_tags
add_tags:
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

#################
# Resume
#################

.PHONY: resume_generate
resume_generate:
	@echo "=== Converting resume.tex to PDF ==="
	@if ! command -v pdflatex >/dev/null 2>&1; then \
		echo "Error: pdflatex not found. Run 'make resume_deps' first."; \
		exit 1; \
	fi
	@cd cv && pdflatex -interaction=nonstopmode -halt-on-error resume.tex > /dev/null 2>&1 || \
		(echo "Error: LaTeX compilation failed. Check cv/resume.log for details." && exit 1)
	@cp cv/resume.pdf static/pdfs/resume.pdf
	@echo "=== PDF generated at cv/resume.pdf and static/pdfs/resume.pdf ==="

.PHONY: resume_clean
resume_clean:
	@echo "=== Cleaning LaTeX auxiliary files ==="
	@rm -f cv/*.aux cv/*.log cv/*.out cv/*.toc
	@echo "Done!"

.PHONY: resume_deps
resume_deps:
	@echo "=== Checking for pdflatex ==="
	@if command -v pdflatex >/dev/null 2>&1; then \
		echo "pdflatex already installed at $$(which pdflatex)"; \
	else \
		echo "pdflatex not found. Installing BasicTeX (~100MB download)..."; \
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
		echo "Then run: make resume_generate"; \
	fi

#################
# Maintenance
#################

.PHONY: todo
todo:
	@echo "=== Searching for TODO items ==="
	@grep -rn "TODO" . \
		--exclude-dir=.git \
		--exclude-dir=node_modules \
		--exclude-dir=public \
		--exclude-dir=resources \
		--exclude-dir=vendor \
		--exclude="*.log" \
		--color=always || echo "No TODO items found"
