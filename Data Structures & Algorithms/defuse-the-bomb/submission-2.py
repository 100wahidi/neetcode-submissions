class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        S=[0]*len(code)
        if k>0:
            for i in range(len(code)):
                if len(code)-i>k:
                    S[i]=sum(code[i+1:i+k+1])
                else:
                    S[i]=sum(code[i+1:])+sum(code[0:k-(len(code)-i)+1])
        elif k<0:
            for i in range(len(code)):
                if i>=abs(k):
                    print(i)
                    S[i]=sum(code[i-abs(k):i])
                else:
                    S[i]=sum(code[0:i])+sum(code[-(abs(k)-i):])

        return S


