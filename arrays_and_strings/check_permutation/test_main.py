import pytest
from .main import is_permutation


@pytest.mark.parametrize("s,t,expected", [
    ("jaime", "aimej", True),
    ("jenny", "ennjy", True),
    ("jaime", "jenny", False)
])
def test_is_permutation(s: str, t: str, expected: bool):
    assert is_permutation(s, t) == expected
