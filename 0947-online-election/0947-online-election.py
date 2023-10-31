class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        ahead_votes = float("-inf")
        candidate = 0 

        count_votes = collections.defaultdict(int)

        i = 0
        j = 0
        self.result = []
        self.times = times
        while j < len(times):
            count_votes[persons[j]] += 1
            if count_votes[persons[j]] >= ahead_votes:
                ahead_votes = count_votes[persons[j]]
                candidate = persons[j]
            self.result.append([times[j], candidate])
            j += 1

    def q(self, t: int) -> int:
        index = bisect.bisect(self.times, t)

        return self.result[index-1][-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)