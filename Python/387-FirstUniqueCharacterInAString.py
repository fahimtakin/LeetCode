class Solution:
    def firstUniqChar(self, s: str) -> int:
        st_map = {}
        for i in range(0, len(s)):  # putting all the values in map
            if s[i] not in st_map:
                st_map[s[i]] = True  # if the value is found then map it to true
            else:
                st_map[s[i]] = False  # if the value is not found then map it to false
        print(st_map)
        for i in range(0, len(s)):  # return the index if the value is found in map
            if st_map[s[i]]:
                return i
        return -1 # if not found then return -1
         
