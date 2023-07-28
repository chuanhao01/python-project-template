from pathlib import Path

from hooks.post_gen_project import generate_license


def test_generate_license(tmp_path: Path):
    # Setting licence dir
    (tmp_path / "_license").mkdir()
    mit_licence_file = tmp_path / "_license" / "mit.txt"
    with open(mit_licence_file, "w+") as f:
        f.write("This is an example mit licence file")

    generate_license(tmp_path, "mit")
    assert tmp_path / "LICENSE"
