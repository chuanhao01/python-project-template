"""Module is called after project is created."""

import subprocess
import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_PATH = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.replace('-', '_') }}"

PROJECT_DESCRIPTION = "{{ cookiecutter.project_description }}"
LICENSE = "{{ cookiecutter.license }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"
AUTHOR_NAME = "{{ cookiecutter.author_name }}"
AUTHOR_EMAIL = "{{ cookiecutter.author_email }}"


def generate_license(project_path: Path, licence: str) -> None:
    """Generate license file for the project.

    Args:
    ----
        project_path: path to the project root directory
        licence: chosen licence
    """
    licences_dict = {
        "MIT": "mit",
        "BSD-3": "bsd3",
        "GNU GPL v3.0": "gpl3",
        "Apache Software License 2.0": "apache",
    }
    move(
        (project_path / "_template" / "licenses" / f"{licences_dict[licence]}.txt").as_posix(),
        (project_path / "LICENSE").as_posix(),
    )


def generate_pyproject(
    project_path: Path,
    project_name: str,
    project_description: str,
    _license: str,
    python_version: str,
    author_name: str,
    author_email: str,
) -> None:
    """Generate pyproject.toml.

    Args:
    ----
        project_path: path to the project root directory
    """
    # Create pyproject.toml
    subprocess.run(
        [
            "poetry",
            "init",
            "--name",
            project_name,
            "--description",
            project_description,
            "--license",
            _license,
            "--author",
            f"{author_name} <{author_email}>",
            "--python",
            f"^{python_version}",
            "-n",
        ],
        check=True,
    )
    # Adding dev packages
    subprocess.run(
        ["poetry", "add", "-G", "dev", "--allow-prereleases", "black@latest", "-n", "--lock"],
        check=True,
    )
    subprocess.run(
        [
            "poetry",
            "add",
            "-G",
            "dev",
            "ruff@latest",
            "mypy@latest",
            "mypy-extensions@latest",
            "coverage@latest",
            "coverage-badge@latest",
            "pytest@latest",
            "pytest-html@latest",
            "pytest-cov@latest",
            "bandit@latest",
            "pre-commit@latest",
            "-n",
            "--lock",
        ],
        check=True,
    )
    # Adding .additional/pyproject toml configs
    with open(project_path / "pyproject.toml", "a", encoding="UTF-8") as pyproject_file:
        pyproject_file.write("\n")

        pyproject_template_path = project_path / "_template" / "pyproject"
        with open(pyproject_template_path / "ruff.toml", encoding="UTF-8") as ruff_file:
            pyproject_file.write(ruff_file.read())
            pyproject_file.write("\n")

        with open(pyproject_template_path / "black.toml", encoding="UTF-8") as black_file:
            pyproject_file.write(black_file.read())
            pyproject_file.write("\n")

        with open(pyproject_template_path / "mypy.toml", encoding="UTF-8") as mypy_file:
            pyproject_file.write(mypy_file.read())
            pyproject_file.write("\n")

        with open(pyproject_template_path / "pytest.toml", encoding="UTF-8") as pytest_file:
            pyproject_file.write(pytest_file.read())
            pyproject_file.write("\n")

        with open(pyproject_template_path / "coverage.toml", encoding="UTF-8") as coverage_file:
            pyproject_file.write(coverage_file.read())
            pyproject_file.write("\n")


def clean_up_template(project_path: Path) -> None:
    """Clean up and remove the _template folder.

    Args:
    ----
        project_path: path to the project root directory
    """
    rmtree((project_path / "_template").as_posix())


def print_futher_instuctions(project_name: str) -> None:
    """Show user what to do next after project creation.

    Args:
    ----
        project_name: current project name
    """
    message = f"""
    Your project {project_name} is created.

    1) Initalize `git` inside your repo

        $ cd {project_name} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) To see additionl commands

        $ make

    -----------------------------

    Do look into the `.addtional` folder for more platform specific templates.
    """
    print(textwrap.dedent(message))


def main() -> None:  # noqa: D103
    generate_license(PROJECT_PATH, LICENSE)
    generate_pyproject(
        PROJECT_PATH,
        PROJECT_NAME,
        PROJECT_DESCRIPTION,
        LICENSE,
        PYTHON_VERSION,
        AUTHOR_NAME,
        AUTHOR_EMAIL,
    )
    clean_up_template(PROJECT_PATH)
    print_futher_instuctions(PROJECT_NAME)


# Ran by the cookiecutter script
if __name__ == "__main__":
    main()
