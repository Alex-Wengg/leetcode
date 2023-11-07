class Solution:
    def smallestSufficientTeam(self, req_skills, people):

        skill_index = { v : i for i,v in enumerate(req_skills)}
        n = len(req_skills)
        dp = { 0 : [] }


        for i, person in enumerate(people):
            curr_skill = 0

            curr_skill = sum( 1 << skill_index.get(skill, 0) for skill in person )

            for prev, needed in dict(dp).items():
                comb = prev | curr_skill
                if comb == prev:
                    continue
                if comb not in dp or len(dp[comb]) > len(needed) + 1:
                    dp[comb] = needed + [i]
            
        return dp[ (1 << n) -1]