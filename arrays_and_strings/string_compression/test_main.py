import pytest
from .main import compress


@pytest.mark.parametrize("s,expected", [
    ("sssbbbfff", "s3b3f3")
])
def test_compress(s: str, expected: str):
    assert compress(s) == expected
