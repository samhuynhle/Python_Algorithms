class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        ret = 0

        for i in xrange(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in xrange(N):
                if grid[i][j]: ret += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ret += best_row + best_col

        return ret