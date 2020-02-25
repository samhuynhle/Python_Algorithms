class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0: return 0
        
        total_rows = len(grid)
        total_cols = len(grid[0])
        number_of_islands = 0
        
        for row_index in range(total_rows):
            for col_index in range(total_cols):
                if grid[row_index][col_index] == '1':
                    number_of_islands += 1
                    self.dfs(grid, row_index, col_index)

        return number_of_islands
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0': return
        
        grid[row][col] = '0'
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)