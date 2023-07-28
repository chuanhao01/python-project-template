"""This module is called after project is created."""

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.replace('-', '_') }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"


def generate_license(directory: Path, licence: str) -> None:
    """Generate license file for the project.

    Args:
        directory: path to the project directory
        licence: chosen licence
    """
    licences_dict = {
        "MIT": "mit",
        "BSD-3": "bsd3",
        "GNU GPL v3.0": "gpl3",
        "Apache Software License 2.0": "apache",
    }
    move(str(directory / "_license" / f"{licences_dict[licence]}.txt"), str(directory / "LICENSE"))
    rmtree(str(directory / "_license"))


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
    pass


if __name__ == "__main__":
    main()
