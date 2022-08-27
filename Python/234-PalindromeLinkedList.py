def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fastPtr = head
        slowPtr = head
        
        # find middle (slow)
        while fastPtr is not None and fastPtr.next is not None:
            fastPtr = fastPtr.next.next # fast pointer increments twice as slow pointer
            slowPtr = slowPtr.next # increments +1
        prevPtr = None   
        #reverse second half
        while slowPtr is not None:
            tmp = slowPtr.next
            slow.next = prevPtr
            prev = slowPtr
            slowPtr = tmp
            
        #check palindrome
        # two pointers coming from two ends and checking for each value
        leftPtr, rightPtr = head, prev
        while rightPtr is not None: 
            if leftPtr.val != rightPtr.val:
                return False
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next
            
        return True
