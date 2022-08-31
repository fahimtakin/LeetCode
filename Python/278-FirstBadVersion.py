# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #binary search
        leftPtr, rightPtr = 1, n # left pointer 1, right pointer is the input
        
        while(leftPtr < rightPtr):
            mid = (leftPtr + rightPtr) // 2 # finding mid point
            if isBadVersion(mid):
                rightPtr = mid
            else:
                leftPtr = mid + 1
        return leftPtr
