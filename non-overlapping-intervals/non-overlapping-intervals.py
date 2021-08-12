class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i : i[1])
        lastEnd = intervals[0][0]
        ans = 0 
        for i in intervals:
            if i[0] >= lastEnd:
                ans += 1 
                lastEnd = i[1]
        return len(intervals)-ans
        