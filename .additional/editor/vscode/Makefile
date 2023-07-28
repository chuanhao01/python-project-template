PATH_TO_PROJECT_ROOT = ../../..

# Help Commands
.PHONY: default
default: help

# Main Commands
.PHONY: install
install:
	ln -srf .vscode $(PATH_TO_PROJECT_ROOT)/
	ln -srf .taplo.toml $(PATH_TO_PROJECT_ROOT)/

.PHONY: install-copy
install-copy:
	cp .vscode $(PATH_TO_PROJECT_ROOT)/
	cp .taplo.toml $(PATH_TO_PROJECT_ROOT)/

.PHONY: help
help:
	@echo 'Usage: make [command]'
	@echo 'install - Install configs using hard symlinks'
	@echo 'install-copy - Install configs by copying files'
