from heapq import *
class Solution:
    def smallestRange(self, lists: List[List[int]]) -> List[int]:
        
        heapp = []
        maxx = -10^5 -1 
        smallest =0
        largest = math.inf

        for i in lists:
            popped = i.pop(0)
            heappush(heapp, [popped, i])
            maxx = max(maxx, popped)
        
        while len(lists) == len(heapp):
            element, arr = heappop(heapp)
            if largest - smallest > maxx - element:
                largest = maxx
                smallest =  element
            
            if len(arr) > 0:
                popped = arr.pop(0)
                
                heappush(heapp, [popped, arr])
                maxx = max(maxx,popped)
            
        return([ smallest,largest])
            
        
         
