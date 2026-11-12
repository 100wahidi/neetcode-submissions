class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash map
        # you track all the sequence with num 
        # pick not seen num and increment boundaries with num
        mp = defaultdict(int)
        res=0
        seen=set()
        for num in nums:
            if num not in seen:
                mp[num]=mp[num-1]+mp[num+1]+1
                mp[num+mp[num+1]]=mp[num]
                mp[num-mp[num-1]]=mp[num]
                res=max(mp[num], res)
                seen.add(num)
        return res

            

        
        