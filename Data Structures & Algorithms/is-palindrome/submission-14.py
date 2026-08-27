class Solution:
    def isPalindrome(self, s: str) -> bool:
        sens = {"?"," ",",","'","/",".",":",";","!"}
        low = s
        for ele in sens:
            low = low.replace(ele,"")
        low = low.lower()
        for i in range(len(low)//2):
            if low[i]!=low[len(low)-1-i]:
                return False
        return True

        