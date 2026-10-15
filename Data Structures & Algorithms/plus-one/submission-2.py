class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=digits[-1]+1
        n=len(digits)
        i=1
        while(i>=0 and digits[n-i]>=10):
            if n-i==0:
                digits[n-i]=1
                digits.append(0)
            else:
                digits[n-i]=digits[n-i]-(digits[n-i]//10)*10
                print(digits[n-i])
                digits[n-i-1]=digits[n-i-1]+1
            i+=1

        return digits