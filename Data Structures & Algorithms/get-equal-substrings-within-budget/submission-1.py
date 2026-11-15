class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        S=0
        L=0
        res=0
        for j in range(len(s)):
            S+=abs(ord(s[j])-ord(t[j]))
            while(L<=j and S>maxCost):
                S-=abs(ord(s[L])-ord(t[L]))
                L+=1
            res=max(res, j-L+1)
        return res
        
