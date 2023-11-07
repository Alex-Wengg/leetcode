class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int total_array_sum = 0;
        for (int num : nums){
            total_array_sum += num;
        }
        int n = nums.size();

        if (total_array_sum % k != 0){
            return false;
        }

        int target_sum = total_array_sum / k;

        vector<int> subsetSum((1 << n), -1);
        subsetSum[0] = 0;

        for (int mask = 0; mask < (1 << n); mask++){
            if (subsetSum[mask] == -1){
                continue;
            }

            for (int i = 0; i < n; i++){
                if ((mask & ( 1 << i)) == 0 & subsetSum[mask] + nums[i] <= target_sum){
                    subsetSum[mask | (1 << i)] = (subsetSum[mask] + nums[i]) % target_sum;
                }
            }

            if(subsetSum[(1 << n) - 1] == 0) { 
                return true;
            }
        }
        return subsetSum[(1 << n) - 1] == 0;
    }
};