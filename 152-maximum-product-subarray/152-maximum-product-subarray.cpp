#include<iostream>
#include<algorithm>
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int r = nums[0];
        
        for(int i=1, maxx = nums[0], minn = nums[0]; i < nums.size(); i++){
            if (nums[i] < 0)
                swap(maxx, minn);
            
            maxx = max(nums[i], nums[i]*maxx);
            minn = min(nums[i], nums[i]*minn);
            
            r = max(r, maxx);
        }
        return r;
    }
};