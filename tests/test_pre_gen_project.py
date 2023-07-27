from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

from hooks.pre_gen_project import validate_project_name


# Unit Test
class TestValidateProjectName:
    def test_invalid_space_name(self):
        with pytest.raises(ValueError):
            validate_project_name("test name")

    def test_invalid_upper_case_name(self):
        with pytest.raises(ValueError):
            validate_project_name("Test-Name")

    def test_invalid_dot_name(self):
        with pytest.raises(ValueError):
            validate_project_name("test.name")

    def test_invalid_starting_number_name(self):
        with pytest.raises(ValueError):
            validate_project_name("2test")

    def test_invalid_ending_hypen_name(self):
        with pytest.raises(ValueError):
            validate_project_name("test-")

    def test_invalid_ending_underscore_name(self):
        with pytest.raises(ValueError):
            validate_project_name("test_")

    def test_valid_generic_name(self):
        validate_project_name("test-n_n2ame")

    def test_valid_ending_number_name(self):
        validate_project_name("test-name2")


# Integration Test
class TestCookiecutterGeneration:
    def test_valid_project_name(self, tmp_path: Path) -> None:
        cookiecutter(
            template=Path.cwd().absolute().as_posix(),
            no_input=True,
            extra_context={"project_name": "valid-project-name"},
            output_dir=tmp_path.absolute().as_posix(),
        )
        assert (tmp_path / "valid-project-name").exists()
        assert (tmp_path / "valid-project-name" / "valid_project_name").exists()

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
