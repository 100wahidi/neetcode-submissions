class Solution(object):
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
        
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Nalph = {" ","`","?","!",",",".", "(",")","{","}",":",";", "/","\\", "@","#", "_","-","|","'",'"', "[","]"}
        s= s.lower()
        input = ""
        for w in s:
            if w not in Nalph:
                input +=w
        ctr = 0
        r = len(input)-1
        l = 0
        while l<r:
            if input[l] != input[r]:
                return self.isPalindrome(input.replace(input[l],"")) or self.isPalindrome(input.replace(input[r],""))
            l+=1
            r-=1
        return True

        
        
        