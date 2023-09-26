from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from hooks.post_gen_project import (
    clean_up_template,
    generate_license,
    generate_pyproject,
    print_futher_instuctions,
)


@pytest.fixture(autouse=True)
def generate_template_path(tmp_path: Path) -> Path:
    """Generate the template folder in the given tmp_path.

    Used to simulate the hook functions running in the template directory after being generated
    """
    template_path = tmp_path / "_template"
    template_path.mkdir(parents=True)
    return template_path


@pytest.fixture
def template_path(generate_template_path: Path) -> Path:
    return generate_template_path


def test_generate_license(tmp_path: Path, template_path: Path) -> None:
    # Setting licence dir
    template_license_path = template_path / "licenses"
    template_license_path.mkdir(parents=True)
    with open(template_license_path / "mit.txt", "w+", encoding="utf-8") as mit_license_file:
        mit_license_file.write("This is an example mit licence file")

    generate_license(tmp_path, "MIT")
    assert (tmp_path / "LICENSE").exists()


def test_generate_pyproject(tmp_path: Path, mocker: MockerFixture, template_path: Path) -> None:
    subprocess_mock = mocker.patch("subprocess.run")

    def create_pyproject_file(*_, **__):
        # Ignore any params, side effect to create the pyproject.toml file
        with open(tmp_path / "pyproject.toml", "w", encoding="utf-8") as pyproject_file:
            pyproject_file.write("pyproject")

    subprocess_mock.side_effect = create_pyproject_file
    # Setting up pyproject templte files
    template_pyproject_path = template_path / "pyproject"
    template_pyproject_path.mkdir(parents=True)
    with open(template_pyproject_path / "pylint.toml", "w+", encoding="utf-8") as pylint_file:
        pylint_file.write("pylint")
    with open(template_pyproject_path / "black.toml", "w+", encoding="utf-8") as black_file:
        black_file.write("black")
    with open(template_pyproject_path / "mypy.toml", "w+", encoding="utf-8") as mypy_file:
        mypy_file.write("mypy")
    with open(template_pyproject_path / "pytest.toml", "w+", encoding="utf-8") as pytest_file:
        pytest_file.write("pytest")
    with open(template_pyproject_path / "coverage.toml", "w+", encoding="utf-8") as coverage_file:
        coverage_file.write("coverage")

    generate_pyproject(
        tmp_path,
        "project_name",
        "project_description",
        "mit",
        "3.11",
        "test_author",
        "test_author@test.com",
    )

    assert subprocess_mock.call_count == 3
    with open(tmp_path / "pyproject.toml", encoding="utf-8") as pyproject_file:
        assert pyproject_file.read() == """pyproject\npylint\nblack\nmypy\npytest\ncoverage\n"""


def test_clean_up_template(tmp_path: Path, template_path: Path) -> None:
    clean_up_template(tmp_path)
    assert not template_path.exists()


def test_print_futher_instuctions(capsys: pytest.CaptureFixture[str]) -> None:
    print_futher_instuctions("valid-project-name")
    capture = capsys.readouterr()
    assert "Your project valid-project-name is created." in capture.out
