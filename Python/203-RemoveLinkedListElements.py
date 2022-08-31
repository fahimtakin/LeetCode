# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head) # create a dummy node which points to head
        prev, curr = dummy, head
        
        while curr: # while the curr pointer is not null
            nxt = curr.next # store the link in a temp value
            if curr.val == val: # if the value matches
                prev.next = nxt # prev points to curr.next
            else:
                prev = curr # if the value doesn't match increment prev
                
            curr = nxt # increment curr
        return dummy.next
                
