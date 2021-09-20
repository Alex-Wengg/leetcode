import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)
        
        totalDays = max(event[1] for event in events)
        
        minHeap = []
        
        day, cnt, eventId = 1, 0, 0
        
        while day  <= totalDays:
            
            if eventId < len(events) and not minHeap:
                day = events[eventId][0]
                
            while eventId < len(events) and events[eventId][0] <= day:
                heapq.heappush(minHeap, events[eventId][1])
                eventId += 1 
            
            while minHeap and minHeap[0] < day:
                heapq.heappop(minHeap)
            
            
            if minHeap:
                heapq.heappop(minHeap)
                cnt += 1
            elif eventId >= len(events):
                break
            day += 1
        return cnt