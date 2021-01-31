import pytest
from typing import Optional, List
from ...data_structures.listnode import ListNode, create_circular_node
from .main import get_loop_start


@pytest.mark.parametrize("head,expected", [
    ([1, 2, 3, 2], 2)
])
def test_get_loop_start(head: List[int], expected: int):
    node: Optional[ListNode] = create_circular_node(head)
    result: Optional[ListNode] = get_loop_start(node)

    assert result.val == expected
