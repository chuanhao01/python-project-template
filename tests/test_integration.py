from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter


class TestCookiecutterGeneration:
    def test_valid_project(self, tmp_path: Path) -> None:
        cookiecutter(
            template=Path.cwd().absolute().as_posix(),
            no_input=True,
            extra_context={
                "project_name": "valid-project-name",
                "project_description": "This is a valid test project description",
                "license": "BSD-3",
                "python_version": "3.11",
                "author_name": "wow username",
                "author_email": "Wowemail@mail.com",
                "line_length": 88,
            },
            output_dir=tmp_path.absolute().as_posix(),
        )

        # Project name and file generated correctly
        project_folder_path = tmp_path / "valid-project-name"
        assert project_folder_path.exists()
        assert (project_folder_path / "valid_project_name").exists()

        # LICENSE file generated correctly
        assert (project_folder_path / "LICENSE").exists()

        # Assert pyproject is generated correctly
        assert (project_folder_path / "pyproject.toml").exists()

        # _template folder cleaned up
        assert not (project_folder_path / "_template").exists()

    def test_invalid_project(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        with pytest.raises(FailedHookException):
            cookiecutter(
                template=Path.cwd().absolute().as_posix(),
                no_input=True,
                extra_context={"project_name": "invalid name"},
                output_dir=tmp_path.absolute().as_posix(),
            )

            capture = capsys.readouterr()
            assert (
                capture.out
                == "ERROR: The project name `invalid name` is not a valid Python module name."
            )
