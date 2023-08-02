"""This module is called after project is created."""

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_PATH = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.replace('-', '_') }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"


def generate_license(project_path: Path, licence: str) -> None:
    """Generate license file for the project.

    Args:
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


def generate_pyproject(project_path: Path)
    """Cleans up and removes the _template folder

    Args:
        project_path: path to the project root directory
    """



def clean_up_template(project_path: Path) -> None:
    """Cleans up and removes the _template folder

    Args:
        project_path: path to the project root directory
    """
    rmtree((project_path / "_template").as_posix())


def print_futher_instuctions(project_name: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
    """
    message = f"""
    Your project {project_name} is created.

    1) Now you can start working on it:

        $ cd {project_name} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) Run codestyle:

        $ make codestyle

    """
    print(textwrap.dedent(message))


def main() -> None:
    generate_license(PROJECT_PATH, LICENSE)
    clean_up_template(PROJECT_PATH)


# Ran by the cookiecutter script
if __name__ == "__main__":
    main()
