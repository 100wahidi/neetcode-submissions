class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window
        # feq and rep>k
        freq=0
        H={}
        L=0
        re=0
        for i in range(len(s)):
            H[s[i]]=H.get(s[i], 0)+1
            freq=max(freq, H[s[i]])
            while(i-L+1-freq>k):
                H[s[L]]=H.get(s[L], 0)-1
                L+=1
            re=max(re, i-L+1)

        
        return re

        
        

            



        
        