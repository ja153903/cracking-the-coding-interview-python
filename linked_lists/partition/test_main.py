import pytest
from typing import Optional, List
from .main import partition
from ...data_structures.listnode import ListNode, list_to_listnode, listnode_to_list


@pytest.mark.parametrize("head,pivot,expected", [
    ([3, 5, 8, 5, 10, 2, 1], 5, [3, 2, 1, 5, 8, 5, 10])
])
def test_partition(head: List[int], pivot: int, expected: List[int]):
    node: Optional[ListNode] = list_to_listnode(head)
    result: Optional[ListNode] = partition(node, pivot)
    result_list: List[int] = listnode_to_list(result)

    assert result_list == expected
