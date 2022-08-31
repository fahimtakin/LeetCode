class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # base case

        for i in range(numRows - 1):  # How many rows
            temp = [0] + res[-1] + [0]  # building a temporary array
            row = []
            for j in range(len(res[-1]) + 1):  # build next row
                row.append(temp[j] + temp[j + 1])  # add the two values
            res.append(row)

        return res
