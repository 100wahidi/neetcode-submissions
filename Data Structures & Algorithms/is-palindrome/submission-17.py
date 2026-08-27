class Solution:
    def isPalindrome(self, s: str) -> bool:
        sens = {"?"," ",",","'","/",".",":",";","!"}
        l,r=0,len(s)-1
        while l<r:
            while l<r and s[l] in sens:
                l+=1
            while l<r and s[r] in sens:
                r-=1
            if s[r].lower()!=s[l].lower():
                return False
            l+=1
            r-=1
        return True
        