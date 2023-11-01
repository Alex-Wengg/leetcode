class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        a.sort()
        b.sort()
        result = []

        a_i = 0
        b_i = 0

        while a_i < len(a) and b_i < len(b):
            a_s, a_e = a[a_i]
            b_s, b_e = b[b_i]
            if max(a_s,   b_s) <= min(a_e, b_e):
                result.append([max(a_s, b_s), min(a_e, b_e)])

            if a_e <= b_e:
                a_i += 1
            else:
                b_i += 1
        
    
        return result

