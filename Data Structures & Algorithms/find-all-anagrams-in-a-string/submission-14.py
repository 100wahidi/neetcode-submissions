class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window=[0]*26
        code=[0]*26
        res=[]
        for i in range(len(p)):
            code[abs(ord(p[i])-97)]+=1
        for j in range(len(s)):
            if j<=len(p)-1:
                window[abs(ord(s[j])-97)]+=1
            else:
                window[abs(ord(s[j])-97)]+=1
                window[abs(ord(s[j-len(p)])-97)]-=1
            if str(window)==str(code):
                res.append(j-len(p)+1)
        return res

                

