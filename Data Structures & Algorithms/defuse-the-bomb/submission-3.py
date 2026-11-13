class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        S=[0]*len(code)
        n=len(code)
        for i in range(len(code)):
            size=abs(k)
            for j in range(1, size+1):
                if k>0:
                    S[i]+=code[(i+j)%n]
                else:
                    S[i]+=code[(i-j)%n]
        return S




