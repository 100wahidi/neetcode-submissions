class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        H_map={}
        Length=10**4
        
        Cs=0
        for i, num in enumerate(nums):
            Cs+=num
            Diff=Cs
            index=0

            if Cs>=target:
                if i==0:
                    return 1
                # binary search for the ferst occurence of sum less than k
                low, high=0, i-1
                while(low<=high):
                    middle=(low+high)//2
                    # the largest min cs of k
                    if H_map[middle]>=Cs-target:
                        high=middle-1
                    else:
                        low=middle+1
                if H_map[low]==Cs-target:
                    Length=min(Length, i-low)  
                elif H_map[low]>Cs-target:
                    Length=min(Length, i-low+1) 
            H_map[i]=Cs
        if Length==10000:
            return 0
        print(H_map)
        return Length

        