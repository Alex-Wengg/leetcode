class Solution {
public:
    bool canConstruct(string s, int k) 
    {
        if(s.size()<k)
        {
            return false;
        }
        int n=s.size();
        int odd_count=0;
        vector<int>v(26,0);
        for(int i=0;i<s.size();i++)
        {
            v[s[i]-97]++;
        }
        for(int i=0;i<26;i++)
        {
            if(v[i]%2==1)
            {
                odd_count++;
            }
        }
        return odd_count<=k;
    }
};