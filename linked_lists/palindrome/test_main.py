import pytest
from typing import Optional, List
from ...data_structures.listnode import ListNode, list_to_listnode
from .main import is_palindrome


@pytest.mark.parametrize("head,expected", [
    ([1, 2, 3, 4], False),
    ([1, 2, 1], True)
])
def test_is_palindrome(head: List[int], expected: bool):
    node: Optional[ListNode] = list_to_listnode(head)

    result: bool = is_palindrome(node)

    assert result == expected
