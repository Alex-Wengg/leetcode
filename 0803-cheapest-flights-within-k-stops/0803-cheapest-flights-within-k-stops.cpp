class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        vector<int>next(n, INT_MAX/2);
        next[src] = 0;

        for (int k = 0; k < K+1; k++){
            vector<int> dp_temp(next);
            for (auto ticket: flights){
                next[ticket[1]] = min(next[ticket[1]], dp_temp[ticket[0]]+ticket[2]);
            }
        }
        if (next[dst] != INT_MAX/2){
            return next[dst];
        }
        return -1;

    }
};