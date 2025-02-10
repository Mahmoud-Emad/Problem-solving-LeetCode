# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        size = 0
        head_ = head
        while head_ is not None:
            head_ = head_.next
            size += 1

        tmp_size = 0
        head_ = head
        while head_ is not None:
            if tmp_size == size // 2:
                return head_

            head_ = head_.next
            tmp_size += 1