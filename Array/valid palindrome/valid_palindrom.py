class Solution:
    def checkAlnum(self, s):
        code = ord(s)

        return (
            48 <= code <= 57 or # number
             65<= code <= 90 or # a to z
             97 <= code <=122 # A to Z
        )
    
    def isPalindrom(self, s):
        l=0
        r = len(s)-1
        while(l<r):
            while l < r and not self.checkAlnum(s[l]):
                l +=1
            while l < r and not self.checkAlnum(s[r]):
                r -=1

            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        
        return True


res = Solution()
print(res.isPalindrom("A man, a plan, a canal: Panama"))