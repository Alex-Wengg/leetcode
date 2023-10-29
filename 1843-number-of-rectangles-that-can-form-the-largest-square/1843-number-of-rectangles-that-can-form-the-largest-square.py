class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # 2 paths 
        # path 1, 4 squares sharing a same element
        # path 2, 
        max_ = 0 
        cnt = 0 
        for l, w in rectangles:
            side = min(l, w)
            if side > max_:
                max_ = side 
                cnt = 1
            elif side == max_:
                cnt += 1
        return cnt 
