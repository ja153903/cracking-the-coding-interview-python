import pytest
from typing import List, Optional
from ...data_structures.listnode import ListNode, listnode_to_list, list_to_listnode
from .main import remove_dups


@pytest.mark.parametrize("head,expected", [
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1], [1]),
    ([1, 1, 1, 1], [1])
])
def test_remove_dups(head: List[int], expected: List[int]):
    head_node: Optional[ListNode] = list_to_listnode(head)

    remove_dups(head_node)

    nums: List[int] = listnode_to_list(head_node)

    assert nums == expected
