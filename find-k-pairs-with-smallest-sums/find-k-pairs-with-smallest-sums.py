class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heapp = []
        for i in nums1:
            for j in nums2:
                summ = i + j
                if len(heapp) < k:
                    heappush(heapp, [-i-j,i,j])
                else:
                    if  i + j > -heapp[0][0]:
                        break
                    else:
                        heappop(heapp)
                        heappush(heapp, [-i-j, i,j])
        result = []
        for summ, i, j in heapp:
            result.append([i,j])
            
        return result
    
    
    
        # def kSmallestPairs(self, nums1, nums2, k, heap=[]):
        # for n1 in nums1:
        #     for n2 in nums2:
        #         if len(heap) < k: heapq.heappush(heap, (-n1-n2, [n1, n2]))
        #         else:
        #             if heap and -heap[0][0] > n1 + n2:
        #                 heapq.heappop(heap)
        #                 heapq.heappush(heap, (-n1-n2, [n1, n2]))
        #             else: break
        # return [heapq.heappop(heap)[1] for _ in range(k) if heap]