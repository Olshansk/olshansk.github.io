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
hugo_server:  ## Run Hugo server
	hugo server -D

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
