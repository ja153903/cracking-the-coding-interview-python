from typing import Optional
from ...data_structures.listnode import ListNode


def remove_dups(head: Optional[ListNode]):
    curr: Optional[ListNode] = head
    prev: Optional[ListNode] = None

    while curr:
        if not prev:
            prev = curr
            curr = curr.next
        else:
            if prev.val == curr.val:
                # if the value is the same, we can just keep iterating
                curr = curr.next
            else:
                # if the values are not the same
                # then prev.next has to be curr
                # then we have to update prev and curr
                prev.next = curr
                prev = curr
                curr = curr.next

    # the edge case here is when the linked list only contains
    # the same value. when we only have the same value this means
    # that we did not update the next pointer to prev
    # so we can do that here
    if prev:
        prev.next = None
