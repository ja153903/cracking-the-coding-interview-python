import pytest
from .main import has_unique_chars


@pytest.mark.parametrize("s,expected", [
    ("aaaaa", False),
    ("", True),
    ("abcd", True),
    ("abcdea", False)
])
def test_has_unique_chars(s: str, expected: bool):
    assert has_unique_chars(s) == expected
