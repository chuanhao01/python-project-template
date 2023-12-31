import pytest

from hooks.pre_gen_project import validate_line_length, validate_project_name


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


class TestValidateLineLength:
    def test_invalid_line_length_lt(self):
        with pytest.raises(ValueError):
            validate_line_length(49)

    def test_invalid_line_length_gt(self):
        with pytest.raises(ValueError):
            validate_line_length(400)

    def test_valid_line_length(self):
        validate_line_length(88)
        validate_line_length(100)
