import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - Scan each cell in grid.
        - If "1" is found, initiate BFS if the cell is not visited.
        - The number of BFS calls == number of islands.
        """
        if not grid:
            return 0
        self.max_i = len(grid)
        self.max_j = len(grid[0])
        self.grid = grid
        self.visited = {}
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for i in range(self.max_i):
            for j in range(self.max_j):
                if self.is_island(i, j) and (i, j) not in self.visited:
                    self.bfs(i, j)
                    islands += 1

        return islands

    def bfs(self, i: int, j: int):
        queue = collections.deque()
        queue.append((i, j))
        self.visited[(i, j)] = True

        while queue:
            n = queue.popleft()
            if self.is_island(n[0], n[1]):
                for adj in self.get_adjacent(n[0], n[1]):
                    if self.is_island(adj[0], adj[1]) and adj not in self.visited:
                        queue.append(adj)
                        self.visited[adj] = True

    def is_island(self, i, j):
        return self.grid[i][j] == "1"

    def get_adjacent(self, i, j):
        def inbounds(di, dj):
            return i + di in range(self.max_i) and j + dj in range(self.max_j)

        return [(i + di, j + dj) for di, dj in self.directions if inbounds(di, dj)]


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

grid3 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "1"],
]

print(Solution().numIslands(grid))
print(Solution().numIslands(grid2))
