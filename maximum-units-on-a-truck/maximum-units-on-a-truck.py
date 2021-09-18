class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        a = sorted(boxTypes,key = lambda x: (-x[1]) )
        s = 0
        print(a)
        for i in a:
            if (truckSize < i[0]):
                s = s+ (i[1]*(truckSize))
                break
            else:
                truckSize -= i[0]
                s = s + (i[1]*i[0])
        return s