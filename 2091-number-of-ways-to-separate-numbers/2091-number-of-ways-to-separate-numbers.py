class Solution:
    mod = 1000000007

    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        if num[0] == '0':
            return 0

        sub = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    sub[i][j] = sub[i + 1][j + 1] + 1

        pref = [[0] * n for _ in range(n)]
        for i in range(n):
            pref[0][i] = 1

        def comp(i, j, length, sub, s):
            com = sub[i][j]
            if com >= length:
                return True
            if s[i + com] < s[j + com]:
                return True
            return False

        def add(a, b):
            return (a + b) % Solution.mod

        for i in range(1, n):
            if num[i] == '0':
                pref[i] = pref[i - 1]
                continue
            for j in range(i, n):
                length = j - i + 1
                preSt = i - 1 - (length - 1)
                count = 0

                if preSt < 0:
                    count += pref[i - 1][i - 1]
                else:
                    count += add(pref[i - 1][i - 1], -pref[preSt][i - 1])

                    if comp(preSt, i, length, sub, num):
                        tempCount = pref[preSt][i - 1] if preSt <= 0 else add(pref[preSt][i - 1], -pref[preSt - 1][i - 1])
                        count = add(tempCount, count)

                pref[i][j] = add(pref[i - 1][j], count)

        return pref[n - 1][n - 1]


