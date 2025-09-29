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
