class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = 0
        f2 = 0
        for i in reversed(cost):
            f1, f2 = i + min(f1, f2), f1 # fancy python swap
        return min(f1, f2)


    def maxCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0
        for i in reversed(cost):
            temp = f1
            f1 = i + max(f1, f2)
            f2 = temp
        return max(f1, f2)