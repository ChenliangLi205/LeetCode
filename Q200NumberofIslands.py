class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        toVisit = []
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                toVisit.append((i,j))
        results = 0
        while len(toVisit):
            i,j = toVisit.pop(0)
            if visited[i][j]:
                continue
            visited[i][j] = True
            if grid[i][j] == "1":
                results += 1
                edges = [(i,j)]
                while len(edges):
                    i_, j_ = edges.pop(0)
                    if i_ - 1 >= 0:
                        if not visited[i_-1][j_]:
                            visited[i_-1][j_] = True
                            if grid[i_-1][j_] == "1":
                                edges.append((i_-1, j_))
                    if i_ + 1 < len(grid):
                        if not visited[i_+1][j_]:
                            visited[i_+1][j_] = True
                            if grid[i_+1][j_] == "1":
                                edges.append((i_+1, j_))
                    if j_ - 1 >= 0:
                        if not visited[i_][j_-1]:
                            visited[i_][j_-1] = True
                            if grid[i_][j_-1] == "1":
                                edges.append((i_, j_-1))
                    if j_ + 1 < len(grid[0]):
                        if not visited[i_][j_+1]:
                            visited[i_][j_+1] = True
                            if grid[i_][j_+1] == "1":
                                edges.append((i_, j_+1))
        return results