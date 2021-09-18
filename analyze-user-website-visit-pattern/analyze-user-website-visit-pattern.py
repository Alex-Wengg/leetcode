class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
                    
        users = {}
        sorted_values = []
        
        # nlog(n)
        for name, stamp, site in zip(username, timestamp, website):
            sorted_values.append([stamp, name, site])
        sorted_values.sort(key = lambda x :x[0])

        # o(n)
        for i in range(len(sorted_values)):
            stamp, name, site = sorted_values.pop(0)
            if name in users:
                users[name].append(site)
            else:
                users[name] = [site]
        
        frequency = {}
		#o(n^3)
        for user, sites in users.items():
            if len(sites) < 3:
                continue
            seen = set()
            for i in range(len(sites)):
                for j in range(i + 1, len(sites)):
                    for k in range(j + 1, len(sites)):
                        seen.add((sites[i], sites[j], sites[k]))
            for pattern in seen:
                if pattern not in frequency:
                    frequency[pattern] = 0
                frequency[pattern] += 1
                
		#o(n)
        return min(frequency, key=lambda x: (-frequency[x], x))
	