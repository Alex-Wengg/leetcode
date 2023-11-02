class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        if not intervals:
            return True
        prevStart, prevEnd = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prevEnd <= start:
                prevStart, prevEnd = intervals[i]

                continue
            else:
                return False
        return True
