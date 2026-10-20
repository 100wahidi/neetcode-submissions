public class Solution
{   
    
    public int Dfs(int i, int n, Dictionary<int,int> L)
    {   
        if (i == n){return 1;}
        if (i > n){return 0;}
        if(L.ContainsKey(i)){return L[i];}
        else{L.Add(i,Dfs(i+1,n, L)+Dfs(i+2,n, L));return L[i];}
    }

    public int ClimbStairs(int n)
    {   Dictionary<int,int> L= new Dictionary<int,int>();
        return Dfs(0,n,L);
    }
}