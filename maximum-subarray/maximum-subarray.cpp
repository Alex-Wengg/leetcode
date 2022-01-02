class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int largest = nums.at(0);
        int curr = 0;
        
        for (auto num: nums){
            if (curr < 0)
                curr = 0;
            curr += num;
            largest = max(curr, largest);
        }
        return largest;
    }
};