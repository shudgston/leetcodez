from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        return reverse_iter(head)


def reverse_iter(node: ListNode) -> ListNode:
    # Use 2 ptrs, but prev starts to the left of head
    prev = None
    curr = node

    while curr is not None:
        # Save the next node before we sever it
        curr_next = curr.next
        # Point next to the prev node
        curr.next = prev
        # Advance prev to current
        prev = curr
        # Advance current to the original next
        curr = curr_next
    return prev


def reverse_recursive(head: ListNode):
    if head is None:
        return head

    new_head = head

    if head.next is not None:
        new_head = reverse_recursive(head.next)
        head.next.next = head

    head.next = None
    return new_head
