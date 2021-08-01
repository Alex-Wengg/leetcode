class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)


        # heaps for finding the maximum start and end
        maxStartHeap, maxEndHeap = [], []

        result = [-1 for x in range(n)]
        for endIndex in range(n):
            heappush(maxStartHeap, (-intervals[endIndex][0], endIndex))
            heappush(maxEndHeap, (-intervals[endIndex][1], endIndex))

        # go through all the intervals to find each interval's next interval
        for _ in range(n):
            # let's find the next interval of the interval which has the highest 'end'
            topEnd, endIndex = heappop(maxEndHeap)
            # result[endIndex] = -1  # defaults to - 1
            if -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
                # find the the interval that has the closest 'start'
                while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                    topStart, startIndex = heappop(maxStartHeap)
                result[endIndex] = startIndex
                # put the interval back as it could be the next interval of other intervals
                heappush(maxStartHeap, (topStart, startIndex))

        return result