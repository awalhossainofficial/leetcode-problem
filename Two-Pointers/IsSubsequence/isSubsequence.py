# A subsequence of a string is a new string that is formed
# from the original string by deleting some (can be none) of the characters without disturbing
# the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# s = "abc"
# t = "ahdbefc"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        while r < len(t):
            if l < len(s) and s[l] == t[r]:
                l += 1
            r += 1
        return l == len(s)
