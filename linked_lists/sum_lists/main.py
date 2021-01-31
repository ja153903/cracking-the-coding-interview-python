from typing import Optional
from ...data_structures.listnode import ListNode


def sum_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result: Optional[ListNode] = ListNode(val=0)
    runner: Optional[ListNode] = result
    carry: int = 0

    while l1 or l2:
        curr_val: int = carry

        if l1:
            curr_val += l1.val
            l1 = l1.next

        if l2:
            curr_val += l2.val
            l2 = l2.next

        runner.next = ListNode(val=curr_val % 10)
        carry = curr_val // 10

        runner = runner.next

    if carry:
        runner.next = ListNode(val=carry)

    return result.next
