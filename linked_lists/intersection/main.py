from typing import Optional
from ...data_structures.listnode import ListNode


def has_intersection(l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
    if not l1 or not l2:
        return False

    A, B = l1, l2

    A_runner, B_runner = A, B

    while A_runner and B_runner:
        if A_runner == B_runner:
            return True

        if not A_runner.next:
            A_runner = B

        if not B_runner.next:
            B_runner = A

        A_runner = A_runner.next
        B_runner = B_runner.next

    return False
