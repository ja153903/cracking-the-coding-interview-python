import pytest
from typing import Optional, List
from ...data_structures.listnode import ListNode, list_to_listnode, listnode_to_list
from .main import delete_middle_node


@pytest.mark.parametrize("middle,expected", [
    ([1, 2, 3], [1, 3])
])
def test_delete_middle_node(middle: List[int], expected: List[int]):
    middle_node: Optional[ListNode] = list_to_listnode(middle)

    delete_middle_node(middle_node.next)

    result: List[int] = listnode_to_list(middle_node)

    assert result == expected
