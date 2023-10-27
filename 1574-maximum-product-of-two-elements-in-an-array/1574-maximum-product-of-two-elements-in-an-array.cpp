class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int mx1 = 0;
        int mx2 = 0;
        for (int n : nums){
            if (n > mx1){
                mx2 = mx1; 
                mx1 = n;
            } else if (n > mx2){
                mx2 = n;
            }

        }
        return (mx1 - 1 ) * (mx2 - 1);
    }
};