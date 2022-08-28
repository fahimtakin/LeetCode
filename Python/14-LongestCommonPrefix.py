class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "" # initially no common
        for i in range(len(strs[0])): # looping through all the letters of the first element
            for s in strs: # looping through all the strings
                if i == len(s) or s[i] != strs[0][i]: # checking if index is out of bound or index of arbirary string is not equal to the strings
                    return res
            res += strs[0][i]
        return res
