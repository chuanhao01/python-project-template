from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter


class TestCookiecutterGeneration:
    def test_valid_project_name(self, tmp_path: Path) -> None:
        cookiecutter(
            template=Path.cwd().absolute().as_posix(),
            no_input=True,
            extra_context={"project_name": "valid-project-name"},
            output_dir=tmp_path.absolute().as_posix(),
        )

        # Project name and file generated correctly
        project_folder_path = tmp_path / "valid-project-name"
        assert project_folder_path.exists()
        assert (project_folder_path / "valid_project_name").exists()

        # LICENSE file generated correctly
        assert (project_folder_path / "LICENSE").exists()
        assert not (project_folder_path / "_licenses").exists()

    def test_invalid_project_name(self, tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
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
