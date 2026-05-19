class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        currRow = 0
        step = 0
        rows = [""] * numRows
        for i in range(len(s)):
            rows[currRow] +=s[i]
            if currRow == 0:
                step = 1
            elif currRow == (numRows-1):
                step = -1
            currRow +=step
        return ("").join(rows)



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for r in range(numRows):
            inc = 2 * (numRows-1)
            for i in range(r, len(s), inc):
                res +=s[i]
                if (r > 0 and r < numRows-1 and 
                    i + inc - 2*r <len(s)):
                    res +=s[i + inc - 2*r]

        return res

