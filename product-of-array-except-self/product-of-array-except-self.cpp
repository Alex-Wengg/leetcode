class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 1);
        
        int prefix = 1;
        for(int i=0; i < nums.size(); i++){
            res.at(i) = prefix;
            prefix *= nums.at(i);
        }
        
        int postfix = 1;
        for(int i=nums.size()-1; i>=0; i--){
            res.at(i) *= postfix;
            postfix *= nums.at(i);
        }
        return res;
    }
};