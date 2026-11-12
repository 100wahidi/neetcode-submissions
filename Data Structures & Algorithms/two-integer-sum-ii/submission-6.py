class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            low, high=i+1, len(numbers)-1
            while(low<=high):
                middle=(low+high)//2
                if numbers[middle]>=target-numbers[i]:
                    high=middle-1
                else:
                    low=middle+1
            if low<len(numbers) and numbers[low]+numbers[i]==target:
                return [i+1, low+1]
                

        