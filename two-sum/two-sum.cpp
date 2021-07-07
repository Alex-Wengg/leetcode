
#include <map>
#include <iostream>
#include <cassert>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> m;
        vector <int> n2;

        for(int i=0; i < nums.size(); i++ ){
            if ( m.find(target-nums[i]) == m.end() ) {
                m.insert(pair<int, int>(nums[i], i));

            }else{
                n2.push_back(m[target-nums[i]]);
                n2.push_back(i);
                return n2;
            }
        }
        return n2;

        
    }
};
