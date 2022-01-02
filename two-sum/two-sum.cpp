class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        vector<int> result;
        
        for (int i= 0; i < nums.size(); i++ ){
            int num = nums.at(i);
            if (umap.find(num) == umap.end()){
                umap[target-num] = i;
            }else{
                result.push_back(umap[num]);
                result.push_back(i);

            }
        }
    return result;
        
    }
};