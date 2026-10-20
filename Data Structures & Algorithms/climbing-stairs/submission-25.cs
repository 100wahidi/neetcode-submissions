public class Solution
{
    public int ClimbStairs(int n)
    {
      if(n==1 || n==0)
      {return 1;}
      else{
      int first=1;
      int second=2;
      for(int i=3;i<=n;i++)
      {
        int curr=first+second;
        first=second;
        second=curr;
      }
      return second;
      }
      
    }
}