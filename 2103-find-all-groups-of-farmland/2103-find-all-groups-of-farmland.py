class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        result = []
        m = len(land)
        for i in range(len(land)):

            for j in range(len(land[0])):

                if land[i][j] == 1:
                    boundary_j = j
                    while boundary_j < len(land[0]) and land[i][boundary_j] == 1:
                        boundary_j += 1
                    
                    boundary_i = i
                    while boundary_i < len(land) and land[boundary_i][j] == 1:
                        boundary_i += 1

                    boundary_i = boundary_i if boundary_i == 0 else boundary_i-1
                    boundary_j = boundary_j  if boundary_j  == 0 else boundary_j  - 1 
                    for wipe_i in range(i, 1+boundary_i):

                        for wipe_j in range(j, 1+boundary_j):
                            land[wipe_i][wipe_j] = 0
                    result.append([i, j, boundary_i, boundary_j])

        return result