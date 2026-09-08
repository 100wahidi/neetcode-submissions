class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        max = 0
        while left < right:
            ctr = min(heights[left],heights[right])*(right-left)
            if ctr > max:
                max = ctr
            if heights[left]>=heights[right]:
                right-=1
            else:
                left+=1
                
        return max
                

