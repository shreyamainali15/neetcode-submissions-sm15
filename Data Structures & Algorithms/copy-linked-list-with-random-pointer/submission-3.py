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
        newCopy = {None:None}
        curr = head

        while curr:
            copy = Node(curr.val)
            newCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = newCopy[curr]
            copy.next = newCopy[curr.next]
            copy.random = newCopy[curr.random]
            curr = curr.next

        return newCopy[head]
        