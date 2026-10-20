public class Solution {
    // Fibonachi 
    public int ClimbStairs(int n) { 
        double left=((double)Math.Sqrt(5)+1)/2;
        double right=(1-(double)Math.Sqrt(5))/2;
        double res= ((double)Math.Pow(left,n+1)-(double)Math.Pow(right,n+1))/(double)Math.Sqrt(5);
        return (int)res;
    }

}
