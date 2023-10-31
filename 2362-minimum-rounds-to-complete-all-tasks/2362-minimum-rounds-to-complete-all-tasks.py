class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = collections.Counter(tasks)

        cnt = 0 

        for k, v in count.items():
            if v == 1:
                return -1
            cnt += math.ceil(v / 3)
        return cnt