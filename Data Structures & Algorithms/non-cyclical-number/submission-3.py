class Solution:
    def isHappy(self, n: int) -> bool:
        i=1
        D=[]
        num=n
        m=set()
        while(num!=0):
            s=0
            while(num*10>0):
                a=num//10
                b=a*10
                D.append(num-b)
                s+=(num-b)**2
                num=a
                i+=1
            if s==1:
                return True
            if s in m:
                return False
            m.add(s)
            num=s

        return False