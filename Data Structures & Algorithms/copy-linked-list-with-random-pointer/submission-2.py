"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        openToNew = {None:None}
        curr = head

        while curr:
            copy = Node(curr.val)
            openToNew[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = openToNew[curr]
            copy.next = openToNew[curr.next]
            copy.random = openToNew[curr.random]
            curr = curr.next

        return openToNew[head]
