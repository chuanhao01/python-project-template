<!-- Disabled markdownlint ruls, for custom numbering of commands -->
<!-- markdownlint-disable MD029 -->

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quickstart

1. Initalize `git` inside your repo

```bash
cd {project_name} && git init
```

2. If you don't have Poetry installed run:

```bash
make poetry-download
```

3. Initialize poetry and install pre-commit hooks:

```bash
make install
make pre-commit-install
```

4. To see additionl commands

```bash
make
```
