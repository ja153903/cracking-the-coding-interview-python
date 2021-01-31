from typing import Optional
from ...data_structures.listnode import ListNode


def delete_middle_node(middle: Optional[ListNode]):
    if middle and middle.next:
        middle.val = middle.next.val
        middle.next = middle.next.next
