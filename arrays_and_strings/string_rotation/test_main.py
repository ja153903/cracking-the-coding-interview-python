import pytest
from .main import is_rotation


@pytest.mark.parametrize("s,t,expected", [
    ("waterbottle", "erbottlewat", True)
])
def test_is_rotation(s: str, t: str, expected: bool):
    assert is_rotation(s, t) == expected
