class Solution:
    def findAnagrams(self, sequence: str,pattern: str) -> List[int]:
        mapp = {}
  
        for char in pattern:
            if not char in mapp:
                mapp[char] = 0
            mapp[char] += 1
        match =  0
        start = 0 
        track = []
        for end in range(len(sequence)):
      
            if sequence[end] in mapp:
                mapp[sequence[end]] -= 1
                if mapp[sequence[end]] ==0:
                    match += 1
      
            if match == len(mapp):
                track.append(start )
          
      
            if end >= len(pattern) - 1:
          
                if sequence[start] in mapp:
                    if mapp[sequence[start]] == 0:
                        match -= 1
                    mapp[sequence[start]] += 1
                start += 1
        return track
