class Solution:
    def partitionString(self, s: str) -> int:
        
        cnt = 0
        seen_ = set()
        for i in range(len(s)):
            if s[i] in seen_:
                print(seen_)
                cnt += 1
                seen_ = set()
            seen_.add(s[i])
        
        return cnt + 1