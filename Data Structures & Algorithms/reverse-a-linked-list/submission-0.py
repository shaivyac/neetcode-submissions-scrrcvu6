# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = None
        next_node = head
        while next_node:
            tmp = next_node.next #1,
            next_node.next = pointer #null
            pointer = next_node
            next_node = tmp #1
        return pointer
            



