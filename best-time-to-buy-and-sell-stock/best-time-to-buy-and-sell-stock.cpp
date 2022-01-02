class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int maxP = 0;
        
        while (r < prices.size()){
            if (prices.at(l) < prices.at(r)){
                int profit = prices.at(r) - prices.at(l);
                maxP = max(maxP, profit);
            }else{
                l = r;
            }
            r += 1;
        }
        return maxP;
    }
};