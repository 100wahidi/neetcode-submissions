
public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        Dictionary<int, int> cache =new Dictionary<int, int>{};
        int n=cost.Length;
        int minimum(int a, int b){if(a>=b){return b;} else{return a;}}
        int DFs(int i){
            // i have to add a trace index for substracting next seen pos
            // i stores the old ones
           if(i>=n){return 0;}
           if(i==-1){return minimum(DFs(i+1),DFs(i+2));}
           else{
                // Logic of substracting
                if(cache.ContainsKey(i)){return cache[i];}
                cache[i]=cost[i]+minimum(DFs(i+1),DFs(i+2));
                return cache[i];
                    
               }            

        }
        return DFs(-1);
        
    }
}
