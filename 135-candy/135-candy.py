class Solution:
    def candy(self, ratings: List[int]) -> int:
        ''' 
            list = [n], list[i] = a value
            res = 0
            1. res += n
            2. if list[i] > list[i+1]. res+= 1
            3. if list[i-1] < list[i]. res+= 1
            Return small res with the requirements

        '''
        n = len(ratings)
        res = 0
        up = 0
        peak = 0
        down = 0
        
        for i in range(1,n):
            
            if ratings[i-1] < ratings[i]:
                up += 1
                peak = up
                down = 0 
                res += up
            elif ratings[i-1] == ratings[i]:
                up = 0 
                peak = 0 
                down = 0
            elif ratings[i-1] > ratings[i]:
                up = 0 
                down += 1
                res +=  down + (-1 if peak >= down else 0)
        return res + n