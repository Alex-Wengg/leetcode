

unvisited
visiting
visited

loop unvisited
   bfs(unvisited[i], visiting, visited)
   
 bfs(element, visinting, visited)
    visited[element]  = true
    visiting[element]  = true
    loop element neighor
      if bfs(element neighbor) is true
        return true
      elif element neighbor is in visiting 
        return true
  //this is for the next graph / path if current breadth return no cycle
  visitng[element] = false
  return false at the end if not 
