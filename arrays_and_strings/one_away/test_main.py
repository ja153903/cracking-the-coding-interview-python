import pytest
from .main import is_one_edit


@pytest.mark.parametrize("s,t,expected", [
    ("pale", "ple", True),
    ("pales", "pale", True),
    ("pale", "bale", True),
    ("pale", "bake", False),
    ("pales", "ple", False)
])
def test_is_one_edit(s: str, t: str, expected: bool):
    assert is_one_edit(s, t) == expected
