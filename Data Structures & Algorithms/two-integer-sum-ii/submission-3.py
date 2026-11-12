class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Hash_map={}
        for i, num in enumerate(numbers):
            if target-num in Hash_map:
                return sorted([i+1, Hash_map[target-num]])
            Hash_map[num]=i+1
        return []
        