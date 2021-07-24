 
class Solution:
    def threeSum(self, arr):
        triplets = []

        start = 0
        end = len(arr) -1 
        arr.sort()

        for i in range(0, len(arr)): 
            if i > 0 and arr[i-1] == arr[i]:
                continue
            start = i+1 
            end = len(arr) -1   
            while start < end:
                s = arr[start] + arr[end]+ arr[i]
                if s == 0:
                    triplets.append([arr[i], arr[start], arr[end]])
                    end -= 1
                    start += 1
                    while start < end and arr[end+1 ] == arr[end]:
                        end -= 1 
                    while start < end and  arr[start-1] == arr[start]:
                        start += 1 
                elif s > 0:
                    end -= 1 
                elif s < 0:
                    start += 1 
        return triplets

                