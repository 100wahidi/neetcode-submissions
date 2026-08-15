class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=set()
        O = False
        for i in nums:
            if i in d:
                O=True

            d.add(i)
        return O



        