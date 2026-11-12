class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search 
        low, high=0, len(matrix)-1
        while(low<=high):
            middle=(low+high)//2
            if matrix[middle][0]>target:
                high=middle-1
            else:
                low=middle+1
        print(low)
            # search on low-1
        left, right=0, len(matrix[low-1])-1
        while(left<=right):
            middle=(left+right)//2
            if matrix[low-1][middle]>=target:
                right=middle-1
            else:
                left=middle+1
        print(left)
        if left>=len(matrix[low-1]) or matrix[low-1][left]!=target:
            return False
        return True
        return True