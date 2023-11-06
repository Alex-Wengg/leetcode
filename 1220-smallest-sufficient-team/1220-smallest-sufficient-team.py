class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_index = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}

        for i, p in enumerate(people):
            cur_skill = 0
            for skill in p:
                cur_skill |= 1 << skill_index[skill] if skill in skill_index else 0

            for prev, need in dict(dp).items():
                comb = cur_skill | prev
                if comb == prev:
                    continue 
                if comb not in dp or len(dp[comb]) > len(need) + 1:
                    dp[comb] = need + [i]
             
        return dp[(1 <<  len(req_skills)) - 1]       
      