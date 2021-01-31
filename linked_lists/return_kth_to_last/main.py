from typing import Optional, List
from ...data_structures.listnode import ListNode


def kth_to_last(head: Optional[ListNode], k: int) -> int:
    if not head:
        return -1

    values: List[int] = []

    while head:
        values.append(head.val)
        head = head.next

    return values[-k]
