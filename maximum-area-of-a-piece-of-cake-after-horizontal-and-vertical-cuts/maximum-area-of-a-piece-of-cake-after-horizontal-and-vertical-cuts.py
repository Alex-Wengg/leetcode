class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        
        
        def helper(limit, cuts):
            cuts.sort()
            
            maxx = max(limit - cuts[-1], cuts[0])
            
            for i in range(1, len(cuts)):
                maxx = max(maxx, cuts[i]-cuts[i-1])
            return maxx
        vert = helper(w, vCuts)
        horz = helper(h, hCuts)
        return int((vert*horz)%1000000007)