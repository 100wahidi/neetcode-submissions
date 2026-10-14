class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        left, right=0, height[len(height)-1]
        r_map={}

        for j in range(len(height)-1, -1,-1):
            r_map[j]=right
            if height[j]>=right:
                right=height[j]
        
        for i in range(len(height)):
            # find the irght
            if min(left,r_map[i])-height[i]>0:
                total+=min(left,r_map[i])-height[i]
            if height[i]>left:
                left=height[i]
        
        return total