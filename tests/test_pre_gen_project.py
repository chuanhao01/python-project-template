from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

# Unit Test


# Integration Test
class TestCookiecutterGeneration:
    def test_valid_converted_project_name(self, tmp_path: Path) -> None:
        cookiecutter(
            template=Path.cwd().absolute().as_posix(),
            no_input=True,
            extra_context={"project_name": "valid project name"},
            output_dir=tmp_path.absolute().as_posix(),
        )
        assert (tmp_path / "valid-project-name").exists()

    def test_invalid_project_name(self, tmp_path: Path) -> None:
        pass
