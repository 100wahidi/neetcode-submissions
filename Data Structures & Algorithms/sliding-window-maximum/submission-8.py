class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximosat=[]
        maxi=nums[0]
        for i in range(len(nums)-k+1):
            if i>=1:
                if maxi==nums[i-1]:   
                    maxi=-10000        
                    for j in range(i, i+k):
                        maxi=max(maxi, nums[j])
                if maxi<=nums[i+k-1]:
                    maxi=nums[i+k-1]
            else:
                for j in range(i, i+k):
                    maxi=max(maxi, nums[j])

            maximosat.append(maxi)
        return maximosat