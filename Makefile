#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`
PYTHONVERSION := py311

CODEDIRS := hooks tests

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
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n
	poetry run mypy --install-types --non-interactive hooks tests

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

#* Format
.PHONY: format
format:
	poetry run black --config pyproject.toml $(CODEDIRS)

#* Linting
.PHONY: ruff
ruff:
	poetry run ruff check $(CODEDIRS)

.PHONY: ruff-fix
ruff-fix:
	poetry run ruff check --fix $(CODEDIRS)

.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml $(CODEDIRS)

.PHONY: lint
lint: ruff-fix mypy

.PHONY: check-lint
check-lint: ruff mypy

#* Testing
.PHONY: test
test:
	PYTHONPATH=$(PYTHONPATH) poetry run pytest -c pyproject.toml --cov-report=html --cov=$(CODEDIRS)
	poetry run coverage-badge -o assets/images/coverage.svg -f

.PHONY: check-safety
check-safety:
	poetry check
	poetry run safety check --full-report
	poetry run bandit -ll --recursive hooks


.PHONY: update-dev-deps
update-dev-deps:
	poetry add -G dev bandit@latest darglint@latest "isort[colors]@latest" mypy@latest pre-commit@latest pydocstyle@latest pylint@latest pytest@latest pyupgrade@latest safety@latest coverage@latest coverage-badge@latest pytest-html@latest pytest-cov@latest
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
