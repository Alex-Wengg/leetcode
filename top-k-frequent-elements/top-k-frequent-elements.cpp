class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> hm;
        for (int i = 0; i < nums.size(); i++){
            if (hm.find(nums[i]) == hm.end()){
                hm.insert(pair<int, int>(nums[i],  0));
            }    
                
            hm[nums[i]]++;
        }
        
        priority_queue<pair<int, int>> pq;
        
        for (int i = 0; i < nums.size(); i++){
            if (hm.find(nums[i]) != hm.end()){
                pq.push(make_pair( hm[nums[i]], nums[i]));
                hm.erase(nums[i]);
                    }
        }
        vector<int> result;
        for (int i = 0; i < k; i++){
            result.push_back(pq.top().second);
            pq.pop();
        }

        
        return  result;
    }
};