class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        def compare(m, n):
            p,q=1,1
            for x in m:
                p*=ord(x)
            for y in n:
                q*=ord(y)
            return p==q

        for i in range(len(s2)-len(s1)+1):
            stack=list(s1)
            if s2[i] in s1:
                # ensure if s2[i:i+len(s1)] a permutation
               if compare(s1, s2[i:i+len(s1)]):
                    print(s1, s2[i:i+len(s1)])
                    return True
                

        return False
        