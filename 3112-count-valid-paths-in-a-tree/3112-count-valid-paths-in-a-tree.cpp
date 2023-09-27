const long long MX = 100001;
    vector<long long> lpf(MX, 0);

class Solution {
public:
    long long ans = 0;
    vector<vector<int>> adj;

    pair<long long, long long> dfs(long long node, long long par){
        bool prime = lpf[node] == node ;
        long long s0 = 0;
        long long s1 = 0;

        for (auto nei : adj[node]){
            if (nei != par){
                auto[c0,c1] = dfs(nei, node);

                if (prime){
                    ans += s0 * c0;
                }else{
                    ans += s0 * c1 + s1 * c0;
                }
                s0 += c0;
                s1 += c1;
            }
        }
        if (!prime){
            ans += s1;
            return {s0 + 1, s1};
        }else{
            ans += s0;
            return {0, s0 + 1};
        }
    }
    long long countPaths(int n, vector<vector<int>>& edges) {
        adj = std::vector<std::vector<int>>(n+1);

        for (long long i = 2; i < MX; i++){
            if (lpf[i] == 0){
                for(long long j = i; j < MX; j+= i){
                    lpf[j] = i;
                }
            }
        }
        for (auto& edge : edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        ans = 0;
       
        dfs(1LL * 1, 1LL * 0);
        return ans;
    }
};