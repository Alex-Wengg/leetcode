class Solution:
    def numberOfCombinations(self, num: str) -> int:
        mod = 1000000007
        def comp(i , j, length, sub, s):
            com = sub[i][j]
            if (com >= length):
                return True
            if s[i + com] < s[j + com]:  # Compare the characters at position 'i+com' and 'j+com' in 's'
                return True
            return False
        def add(a, b):
            return (a+b) % mod

        n = len(num)
        if num[0] == '0':
            return 0

        sub = [[0 for i in range(n+1)] for j in range(n+1)]
        # sub = [[0] * (n + 1) for _ in range(n + 1)]

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if num[i] == num[j]:
                    sub[i][j] = sub[i+1][j+1] + 1
        '''
        [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        [12, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        [11, 11, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        [10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        [9, 9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        [8, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        [7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1, 0]
        [6, 6, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1, 0]
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0]
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0]
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0]
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'''

        pref = [[0 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            pref[0][i] = 1
        
        for i in range(1, n):
            if num[i] == '0':
                pref[i] = pref[i-1]
                continue
            
            for j in range(i, n):
                length = j - i + 1
                preSt = i - 1 - (length - 1)
                count = 0

                if preSt < 0:
                    count += pref[i-1][i-1]
                else:
                    count += add(pref[i-1][i-1], - pref[preSt][i-1])

                    
                    if comp(preSt, i, length, sub, num):
                        tempCount = pref[preSt][i - 1] if preSt <= 0 else add(pref[preSt][i - 1], -pref[preSt - 1][i - 1])
                        count = add(tempCount, count)
                
                pref[i][j] = add(pref[i-1][j], count)
        return pref[n-1][n-1]
