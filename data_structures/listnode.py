from typing import Optional, List, Dict
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


def listnode_to_list(head: Optional[ListNode]) -> List[int]:
    if not head:
        return []

    result: List[int] = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def list_to_listnode(nums: List[int]) -> Optional[ListNode]:
    result: Optional[ListNode] = ListNode()
    runner: Optional[ListNode] = result

    for num in nums:
        runner.next = ListNode(val=num)
        runner = runner.next

    return result.next


def create_circular_node(nums: List[int]) -> Optional[ListNode]:
    nodes: Dict[int, Optional[ListNode]] = {}
    prev: Optional[ListNode] = None

    for num in nums:
        if num in nodes:
            prev.next = nodes[num]
        else:
            node: Optional[ListNode] = ListNode(val=num)
            prev.next = node
            nodes[num] = node

        prev = nodes[num]

    return nodes[nums[0]]
