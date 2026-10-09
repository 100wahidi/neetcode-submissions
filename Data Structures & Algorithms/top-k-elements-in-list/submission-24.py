class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        s =[]
        for i in range(len(nums)):
            hash_map[nums[i]]=1+hash_map.get(nums[i],0)
        frequencies = list(hash_map.values())
        n = len(frequencies)
        sort = sorted(frequencies)[n-k:]
        for num in hash_map.keys():
            if hash_map[num] in sort:
                s.append(num)
        return s

        
        