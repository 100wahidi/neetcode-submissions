class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        for i in range(len(numbers)):
            temp = target - numbers[i]
            max = len(numbers)-1
            min = i+1
            while  max>=min:
                if numbers[min]==temp:
                    return [i+1,min+1]
                if numbers[max]==temp:
                    return [i+1,max+1]
                ptr = (max+min)//2
                if numbers[ptr]==temp:
                    return [i+1,ptr+1]
                elif numbers[ptr]>temp:
                    max = ptr -1
                elif numbers[ptr]<temp:
                    min = ptr +1
        return []
            
        