public class Solution {
    public int FirstUniqChar(string s) {
        var h_map= new Dictionary<char,int[]>();
        for(int i=0;i<s.Count();i++)
        {
            if(h_map.ContainsKey(s[i]))
            {
             h_map[s[i]][0]=i;
             h_map[s[i]][1]+=1;
            }
            else{
                var L= new int[2]{i,1};
                h_map.Add(s[i], L);
            }
        }
        foreach(char k in h_map.Keys){
            if(h_map[k][1]==1){
                return h_map[k][0];
            }
        }
        return -1;
    }
}