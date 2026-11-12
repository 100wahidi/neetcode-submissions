class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if self.ValidSubseq(s,t):
            return 0
        concat = 0
        l, r=0, len(t)-1
        while(l<=r):
            mid = (l+r)//2
            if self.ValidSubseq(s+t[mid:],t):
                l=mid+1
            else:
                r=mid-1
        return len(t)-r


    def ValidSubseq(self, s: str, t:str):
        R = ""
        i=0
        for e in s:
            if i==len(t):
                break
            if e ==t[i]:
                R+=e
                i+=1
        return R==t

    
    

        