class Solution:

    def leastBricks(self, wall: List[List[int]]) -> int:
        # bruthe force
        H_mp={}
        count=0
        for row in wall:
            Cum=0
            for brick in row:
                Cum+=brick
                H_mp[Cum]=H_mp.get(Cum, 0)+1
        print(H_mp)
        for e, f in H_mp.items():
            if e!=Cum and e!=0:
                count=max(count, f)

        return len(wall)-count



        