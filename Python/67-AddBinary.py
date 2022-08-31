class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = "" # result
        carry = 0
        
        a, b = a[::-1], b[::-1] # reverse the string so we can start adding from LSB
        
        for i in range(max(len(a), len(b))): # run through the longer string
            if i < len(a): # if i is in bound
                digitA = ord(a[i]) - ord("0") #ord() gives the ascii value and by subtracting the ascii value of "0" from the string we are converting to integer
            else:
                digitA = 0 # if no digit left then digit = 0 as it makes no difference

            if i < len(b):  # if i is in bound
                digitB = ord(b[i]) - ord("0")  # ord() gives the ascii value and by subtracting the ascii value of "0" from the string we are converting to integer
            else:
                digitB = 0  # if no digit left then digit = 0 as it makes no difference
                
            total = digitA + digitB + carry
            char = str(total % 2) # modding by two --> base 2, eg: 1 % 2 = 1, 2 % 2 = 0 and carry 1
            res = char + res # add the character to the beginning of results array
            carry = total // 2 # eg: 2//2 = 1, so carry = 1
            
        if carry:
            res = "1" + res
        return res
