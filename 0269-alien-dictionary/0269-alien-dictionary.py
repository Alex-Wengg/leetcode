class Solution:
  def alienOrder(self, words):
    map = {}
    degree = {}
    result = ""

    if (not(words)) :
      return result

    for s in words:
      for c in s:
        degree[c] = 0

    for i in range(len(words)-1):
      cur = words[i]
      next = words[i+1] 
      if len(cur) > len(next) and cur.startswith(next):
        return ""
      length = min(len(cur), len(next))

      for j in range(length):
        c1 = cur[j]
        c2 = next[j]
        if c1 != c2:
          set_ = set()
          if (c1 in map):
            set_ = map[c1]
          
          if c2 not in set_:
            set_.add(c2)
            map[c1] = set_
            degree[c2] = degree.get(c2, 0) + 1 
          
          break
      
    q = []
    for c, v in degree.items():
      if v == 0:
        q.append(c)
      
    while q:
      c = q.pop()
      result += c
      if c in map:
        for c2 in map[c]:
          degree[c2] = degree[c2] -1
          if degree[c2] == 0:
            q.append(c2)
      
    if len(result) != len(degree):
      return ""
    return result 


