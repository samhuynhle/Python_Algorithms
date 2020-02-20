class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbing(0, n)    
    
    def climbing(self, i, n):
        if i > n: return 0
        if i == n: return 1
        return self.climbing(i + 1, n) + self.climbing(i + 2, n)