# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = []
        curr = head

        while curr:
            dummy.append(curr)
            curr = curr.next

        index = len(dummy) - n

        if index == 0:
            return head.next

        dummy[index - 1].next = dummy[index].next

        return head
        