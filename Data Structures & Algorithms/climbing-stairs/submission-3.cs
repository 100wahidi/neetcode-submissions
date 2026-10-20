public class Solution
{   public Dictionary<int,int> L= new Dictionary<int,int>();
    
    public int Dfs(int i, int n)
    {   
        if (i == n){return 1;}
        if (i > n){return 0;}
        if(this.L.ContainsKey(i)){return this.L[i];}
        else{this.L.Add(i,Dfs(i+1,n)+Dfs(i+2,n));return this.L[i];}
    }

    public int ClimbStairs(int n)
    {   
        return Dfs(0,n);
    }
}