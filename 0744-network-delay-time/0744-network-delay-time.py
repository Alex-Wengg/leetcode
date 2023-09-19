from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:












        earliestTime = {}

        for i in range(1, n+1):
            earliestTime[i] = float('inf')
        earliestTime[k] = 0 

        next = defaultdict(list)
        for x,y,z in times:
            next[x].append((y,z))
        
        q = [(k, 0)]
        while q:
            curNode, curTime = q.pop(0)

            if curTime > earliestTime[curNode]:
                continue
            
            for t in next[curNode]:
                nextNode, weight = t
                if earliestTime[nextNode] <= earliestTime[curNode] + weight:
                    continue

                earliestTime[nextNode] = earliestTime[curNode] + weight
                q.append((nextNode, earliestTime[nextNode]))
        
        result = 0 
        for i in range(1, n+1):
            result = max(result, earliestTime[i])
        
        if result == float('inf'):
            return -1
        return result 
