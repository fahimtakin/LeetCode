class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        firstMap = collections.Counter(nums1)  # count how many of which elements are there
        secondMap = collections.Counter(nums2)
        return (firstMap & secondMap).elements()  # return the intersection element and frequencies
