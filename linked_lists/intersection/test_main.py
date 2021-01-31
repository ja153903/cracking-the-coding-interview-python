from typing import Optional
from ...data_structures.listnode import ListNode
from .main import has_intersection

# TODO: Need to create a new function that generates 2 linked lists
# that intersect each other


def test_has_intersection():
    l1: Optional[ListNode] = ListNode(val=1)
    l2: Optional[ListNode] = ListNode(val=2)

    intersecting_node: Optional[ListNode] = ListNode(val=5)

    l1.next = ListNode(val=5)
    l2.next = intersecting_node

    l1.next.next = ListNode(val=3)
    l2.next.next = ListNode(val=4)

    l1.next.next.next = intersecting_node
    l2.next.next.next = ListNode(val=1)

    assert has_intersection(l1, l2) == True
