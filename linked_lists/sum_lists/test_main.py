import pytest
from typing import Optional, List
from ...data_structures.listnode import ListNode, list_to_listnode, listnode_to_list
from .main import sum_lists


@pytest.mark.parametrize("l1,l2,expected", [
    ([7, 1, 6], [5, 9, 2], [2, 1, 9])
])
def test_sum_lists(l1: List[int], l2: List[int], expected: List[int]):
    l1node: Optional[ListNode] = list_to_listnode(l1)
    l2node: Optional[ListNode] = list_to_listnode(l2)

    result: Optional[ListNode] = sum_lists(l1node, l2node)

    result_list: List[int] = listnode_to_list(result)

    assert result_list == expected
