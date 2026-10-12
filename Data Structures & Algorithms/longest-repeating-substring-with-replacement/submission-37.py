class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxisio=0
        count={}
        l=0
        maxf=0
        for j in range(len(s)):
            count[s[j]]=count.get(s[j],0)+1
            maxf=max(count[s[j]], maxf)
            # dynamic window tracking the replacable substrings: if not start the loop
            while(j-l+1-maxf>k):
                count[s[l]]-=1
                l+=1
            maxisio=max(maxisio, j-l+1)

        return maxisio

                


                