import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l ,r , h in buildings:
            events.append((l, -h, r))
            # edge, no more coordinates at the end
            events.append((r,0,0))
            
        events.sort()
        # [[x,y]] corners
        # edge case too 
        res = [[0,0]]
        # [(height, x)]
        # edge case
        hp = [(0, float("inf"))]
        
        for xPos, height, r in events:
            #check the range from minX to maxX in a list
            if height != 0:
                heapq.heappush(hp, (height, r))
            # if xPos is further than the ending rightX then we delete 
            # restart
            while hp[0][1] <= xPos:
                heapq.heappop(hp)
            # append the new corner 
            if res[-1][1] != -hp[0][0]:
                res.append([xPos, -hp[0][0]])
        return res[1:]