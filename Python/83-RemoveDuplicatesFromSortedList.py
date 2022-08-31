# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curPtr = head #curPtr pointing at head
        
        while curPtr: # while curPtr is not null
            while curPtr.next and curPtr.next.val == curPtr.val # while curPtr.next is not null and curPtr.next value is equal to curPtr value
                curPtr.next=curPtr.next.next # curPtr.next is changed
                
            curPtr = curPtr.next 
            
        return head
        
