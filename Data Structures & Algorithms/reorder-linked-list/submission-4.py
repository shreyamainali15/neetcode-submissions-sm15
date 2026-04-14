# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = []
        curr = head

        while curr:
            dummy.append(curr)
            curr = curr.next

        left = 0
        right = len(dummy) - 1

        while left < right:
            dummy[left].next = dummy[right]
            left += 1

            if left == right:
                break

            dummy[right].next = dummy[left]
            right -= 1

        dummy[left].next = None
            