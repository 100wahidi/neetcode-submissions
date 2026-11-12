class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def IsPermutation( s1, s2):
            H={}
            ct=0
            for i in range(len(s1)):
                H[s1[i]]=H.get(s1[i], 0)+1
            for j in range(len(s1)):
                H[s2[j]]=H.get(s2[j], 0)-1
                if H[s2[j]]==0:
                    ct+=1
            return ct==len(H)
        

        for j in range(len(s2)-len(s1)+1):
            if IsPermutation(s1, s2[j:j+len(s1)]):
                return True

        return False

            

            

        