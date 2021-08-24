var visited

loop all the nodes 
  dfs each node
    return true if helper() returns true
  
 
 helper function(node, parent 
  visited = true
  
  loop current node neighbors
    
    if neighor isnt visited then dfs the neighor
      return true if dfs(neighor) is true
    if neighor is visited and not parent
      return true
   return false at the end of loop

