#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

ALLDIRS := tests {{ cookiecutter.project_name.replace("-", "_") }}

# Help Commands
.PHONY: default
default: help

.PHONY: help
help:
	@echo 'Usage: make [command]'
	@echo ''
	@echo 'poetry-download      - Download and install poetry using the curl script'
	@echo 'poetry-remove        - Remove poetry using the curl script'
	@echo '----------------------------------------'
	@echo 'setup                - Setup the venv based on pyenv version'
	@echo 'install              - Run setup and install-only'
	@echo 'pre-commit-install   - Install pre-commit hooks (Using the install poetry package)'
	@echo 'lint                 - Run ruff --fix and mypy'
	@echo 'check-lint           - Run ruff, mypy and bandit'
	@echo 'test                 - Run tests'
	@echo 'check-code           - Run lint and test'
	@echo '----------------------------------------'
	@echo 'cleanup              - Clean up any pycache, mypy, ipynb, pytest artifacts'
	@echo 'build-remove         - Delete build folder'

#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://install.python-poetry.org | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://install.python-poetry.org | $(PYTHON) - --uninstall

#* Installation
.PHONY: install
install:
	python -m venv .venv
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n
	poetry run mypy --install-types --non-interactive hooks tests

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

#* Format
.PHONY: format
format:
	poetry run black --config pyproject.toml $(ALLDIRS)

#* Linting
.PHONY: ruff
ruff:
	poetry run ruff check $(ALLDIRS)

.PHONY: ruff-fix
ruff-fix:
	poetry run ruff check --fix $(ALLDIRS)

.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml $(ALLDIRS)

.PHONY: lint
lint: ruff-fix mypy

.PHONY: check-safety
check-safety:
	poetry check
	poetry run bandit -ll --recursive $(ALLDIRS)

.PHONY: check-lint
check-lint: ruff mypy check-safety

#* Testing
.PHONY: test
test:
	PYTHONPATH=$(PYTHONPATH) poetry run pytest -c pyproject.toml --cov-report=html --cov=$(ALLDIRS)

#* Check Code
.PHONY: check-code
check-code: check-lint test

.PHONY: update-dev-deps
update-dev-deps:
	poetry add -G dev bandit@latest mypy@latest pre-commit@latest pytest@latest coverage@latest pytest-html@latest pytest-cov@latest ruff@latest
	poetry add -G dev --allow-prereleases black@latest

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove
