class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        Max=0
        ptr=1
        nums=sorted(nums)
        for i in range(len(nums)):
            sold=k
            Freq=1
            ptr=1
            while(sold>0):
                if i-ptr>=0 and nums[i]-nums[i-ptr]<=sold:
                    sold-=nums[i]-nums[i-ptr]
                    Freq+=1
                    ptr+=1
                else:
                    break
            print(i, Freq)
            Max=max(Max, Freq)
        return Max
            
                





            