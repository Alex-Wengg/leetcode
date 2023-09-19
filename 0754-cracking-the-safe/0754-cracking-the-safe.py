class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = '0' * (n - 1)
        record = {}

        total = k ** n 

        for i in range(total):
            # temp = ans[len(ans) - (n - 1) : (n- 1)]
            temp = ans[-(n-1):] if n > 1 else ''

            # record[temp] = (record[temp]+1)%k
            record[temp] = (record.get(temp, 0) + 1) % k

            ans +=   str(record[temp])
        return ans