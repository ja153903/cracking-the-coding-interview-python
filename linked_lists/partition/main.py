from typing import Optional, List
from ...data_structures.listnode import ListNode


def partition(head: Optional[ListNode], pivot: int) -> Optional[ListNode]:
    le_partition: List[Optional[ListNode]] = []
    gte_partition: List[Optional[ListNode]] = []

    while head:
        if head.val < pivot:
            le_partition.append(head)
        else:
            gte_partition.append(head)

        head = head.next

    for i in range(1, len(le_partition) + 1):
        if i == len(le_partition):
            le_partition[-1].next = None
        else:
            le_partition[i-1].next = le_partition[i]

    for i in range(1, len(gte_partition) + 1):
        if i == len(gte_partition):
            gte_partition[-1].next = None
        else:
            gte_partition[i-1].next = gte_partition[i]

    if le_partition and gte_partition:
        le_partition[-1].next = gte_partition[0]

    return le_partition[0] if le_partition else (gte_partition[0] if gte_partition else None)
