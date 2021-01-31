import pytest
from .main import urlify


@pytest.mark.parametrize("s,n,expected", [
    ("Mr John Smith    ", 13, "Mr%20John%20Smith")
])
def test_urlify(s: str, n: int, expected: str):
    assert urlify(s, n) == expected
