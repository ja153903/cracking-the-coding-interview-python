from typing import Optional, Set
from ...data_structures.listnode import ListNode


def get_loop_start(head: Optional[ListNode]) -> Optional[ListNode]:
    seen: Set[Optional[ListNode]] = set()

    while head:
        if head in seen:
            return head

        seen.add(head)

        head = head.next

    return None
