from pathlib import Path

from hooks.post_gen_project import generate_license


def test_generate_license(tmp_path: Path) -> None:
    # Setting licence dir
    template_path = tmp_path / "_template"
    (template_path / "licenses").mkdir(parents=True)
    mit_licence_file_path = template_path / "licenses" / "mit.txt"
    with open(mit_licence_file_path, "w+", encoding="utf-8") as mit_license_file:
        mit_license_file.write("This is an example mit licence file")

    generate_license(tmp_path, "MIT")
    assert (tmp_path / "LICENSE").exists()
