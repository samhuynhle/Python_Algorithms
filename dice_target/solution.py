class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        output = 0

        for i in range(1, f +1):
            sum = 1
            if self.isValid(d - 1, f, target, i):
                output += 1
        
        return output % (10**9 + 7)

    def isValid(self, d, f, target, sum):
        if d == 0 and sum == target:
            return True

        if sum < target and d > 0:
            for i in range(1, f + 1):
                if self.isValid(d - 1, f, target, sum + i):
                    return True
        else:
            return False