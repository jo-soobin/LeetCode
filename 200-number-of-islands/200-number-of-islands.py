class Solution:
    def DFS(self, grid, Xindex, Yindex):
        if Xindex < 0 or Yindex < 0:
            return
        if Xindex >= self.Xrange or Yindex >= self.Yrange:
            return
        if grid[Yindex][Xindex] == '0':
            return
        grid[Yindex][Xindex] = '0'
        self.DFS(grid, Xindex, Yindex+1)
        self.DFS(grid, Xindex+1, Yindex)
        self.DFS(grid, Xindex, Yindex-1)
        self.DFS(grid, Xindex-1, Yindex)
    def numIslands(self, grid: List[List[str]]) -> int:
        self.IslandCount = 0
        self.Yrange = len(grid)
        self.Xrange = len(grid[0])
        for Xindex in range(self.Xrange):
            for Yindex in range(self.Yrange):
                if grid[Yindex][Xindex] == '1':
                    self.IslandCount += 1
                    self.DFS(grid, Xindex, Yindex)
        return self.IslandCount