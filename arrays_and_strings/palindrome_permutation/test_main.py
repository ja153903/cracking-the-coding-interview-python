import pytest
from .main import is_palindrome_permutation


@pytest.mark.parametrize("s,expected", [
    ("Tact Coa", True)
])
def test_is_palindrome_permutation(s: str, expected: bool):
    assert is_palindrome_permutation(s) == expected
