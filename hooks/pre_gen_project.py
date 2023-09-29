"""Module is called before project is created."""

import re
import sys

PROJECT_NAME: str = "{{ cookiecutter.project_name }}"
LINE_LENGTH_PARAMETER: str = "{{ cookiecutter.line_length }}"


def validate_project_name(project_name: str) -> None:
    """Ensure that `project_name` parameter is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers hypens or underscores.

    Args:
    ----
        project_name: current project name

    Raises:
    ------
        ValueError: If project_name is not a valid Python module name
    """
    module_regex = re.compile(r"^([a-z]|[a-z][a-z0-9_-]*[a-z0-9])$")
    if module_regex.fullmatch(project_name) is None:
        message = f"ERROR: The project name `{project_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_line_length(line_length: int) -> None:
    """Validate line_length parameter. Length should be between 50 and 300.

    Args:
    ----
        line_length: integer paramenter for isort and black formatters

    Raises:
    ------
        ValueError: If line_length isn't between 50 and 300
    """
    MIN_LINE_LENGTH = 50
    MAX_LINE_LENGTH = 300
    if not MIN_LINE_LENGTH <= line_length <= MAX_LINE_LENGTH:
        message = f"ERROR: line_length must be between 50 and 300. Got `{line_length}`."
        raise ValueError(message)


def main() -> None:  # noqa: D103
    try:
        validate_project_name(project_name=PROJECT_NAME)
        validate_line_length(line_length=int(LINE_LENGTH_PARAMETER))
    except ValueError as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()
