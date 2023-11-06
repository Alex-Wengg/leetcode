class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_index = { v : i for i, v in enumerate(req_skills)}
        dp = { 0 : []}

        for i, person in enumerate(people):
            curr_skill = 0 
            for skill in person:
                curr_skill |= 1 << skill_index[skill] if skill in skill_index else 0
            
            for prev, need in dict(dp).items():
                comb = prev | curr_skill 
                if comb not in dp or len(dp[comb]) > len(need) + 1:
                    dp[comb] = need + [i]

        return dp[ (1 << len(req_skills)) - 1]

