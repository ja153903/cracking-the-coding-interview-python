import pytest
from typing import Optional, List
from ...data_structures.listnode import ListNode, list_to_listnode
from .main import kth_to_last


@pytest.mark.parametrize("head,k,expected", [
    ([1, 2, 3, 4, 5], 2, 4)
])
def test_kth_to_last(head: List[int], k: int, expected: int):
    node: Optional[ListNode] = list_to_listnode(head)

    result: int = kth_to_last(node, k)

    assert result == expected
