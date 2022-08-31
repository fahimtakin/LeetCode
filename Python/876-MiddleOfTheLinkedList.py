# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's Tortoise and Hare Algorithm

        slowPtr, fastPtr = head, head # both start from head

        while (fastPtr != None):  # while fastPtr is not null
            fastPtr = fastPtr.next
            if fastPtr == None:
                return slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

        return slowPtr
        
