#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            if (i > 0 && nums[i] == nums[i-1])
                continue; 
            
            int l = i + 1;
            int r = nums.size() - 1;
            int curr = nums[i];
            while (l < r){
                int summ = curr + nums[l] + nums[r];
                if (summ > 0){
                    r-=1;
                }else if (summ < 0){
                    l+=1;
                }else{
                    res.push_back({curr, nums[l], nums[r]});
                    l++;
                    while (nums[l] == nums[l - 1] && l < r){
                        l+=1;
                    }
                }
            }
        }
        return res;
    }
};