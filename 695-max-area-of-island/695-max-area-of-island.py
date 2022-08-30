class Solution:
    def DFS(self, grid, i, j):
        if self.Height <= i or self.Width <= j:
            # out of range
            return 0
        if i < 0 or j < 0:
            # out of range
            return 0
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        # DFS
        return 1 + self.DFS(grid, i+1, j) + self.DFS(grid, i-1, j) + self.DFS(grid, i, j+1) + self.DFS(grid, i, j-1)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.Height = len(grid)
        self.Width = len(grid[0])
        maxIsland = 0
        for heightIDX in range(self.Height):
            for widthIDX in range(self.Width):
                returnValue = self.DFS(grid, heightIDX, widthIDX)
                if maxIsland < returnValue:
                    maxIsland = returnValue
        return maxIsland