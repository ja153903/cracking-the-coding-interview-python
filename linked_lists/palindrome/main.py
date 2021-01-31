from typing import Optional, List
from ...data_structures.listnode import ListNode


def is_palindrome(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return True

    values: List[int] = []

    while head:
        values.append(head.val)
        head = head.next

    return values == values[::-1]
