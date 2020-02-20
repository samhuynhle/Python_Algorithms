class Solution:
    def climbStairs(self, n):
        memo = [0] * n
        return self.climbing_stairs(0, n, memo)
    
    def climbing_stairs(self, i, n, memo):
        if i > n: return 0
        if i == n: return 1
        if memo[i] > 0: return memo[i]
        
        memo[i] = self.climbing_stairs(i + 1, n, memo) + self.climbing_stairs(i + 2, n, memo)
        return memo[i]
    