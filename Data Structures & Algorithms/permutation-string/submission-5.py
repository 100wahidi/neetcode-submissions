class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        Hash=[0]*26
        Signature=Hash.copy()
        if len(s1)>len(s2):
            return False
        for k in range(len(s1)):
            Signature[abs(ord(s1[k])-ord("a"))]+=1
            Hash[abs(ord(s2[k])-ord("a"))]+=1
        if str(Hash)==str(Signature):
            return True
        for i in range(len(s2)-len(s1)):
            Hash[abs(ord(s2[len(s1)+i])-ord("a"))]+=1
            Hash[abs(ord(s2[i])-ord("a"))]-=1
            if str(Hash)==str(Signature):
                return True

        return False

        