class Solution:
    def smallestSufficientTeam(self, req_skills, people):

        skill_index = { v : i for i,v in enumerate(req_skills)}
        dp = { 0 : [] }

        for i, individal_skills in enumerate(people):
            curr_skill = 0
            for skill in individal_skills:
                curr_skill |= (1 << skill_index[skill] if skill in skill_index else 0 )
            
            for prev, needed in dict(dp).items():
                comb = prev | curr_skill
                if comb == prev:
                    continue
                if comb not in dp or len(dp[comb]) > len(needed) + 1:
                    dp[comb] = needed + [i]
            
        return dp[(1 << len(req_skills)) - 1]