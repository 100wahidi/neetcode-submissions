class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # logic where it exist is  in i-1 where matrix[i][0]>target
        # if all of them are higher it will be 0 else extreme case 
        # is it is highr than all len(products)
        # in normal cases : it is i-1
        # it is enough to map it by i-1
        # and tale first case 0 in consideration with iff to break
        # uttermost optimal Solution:
        low, high=0, len(matrix)-1
        while(low<=high):
            middle=(low+high)//2
            if matrix[middle][0]>target:
                high=middle-1
            else:
                low=middle+1
        print(low)

        bot = low-1
        left, right=0, len(matrix[bot])-1
        while(left<=right):
            ptr=(left+right)//2
            if matrix[bot][ptr]>=target:
                right=ptr-1
            else:
                left=ptr+1
        if left==len(matrix[bot]) or matrix[bot][left]!=target: 
            return False
        print(low)    
        return True    

        