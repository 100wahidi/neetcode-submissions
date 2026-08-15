class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        b = {}
        for i in t:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in s:
            if j not in b:
                b[j]=1
            else:
                b[j]+=1

        return b==d

            