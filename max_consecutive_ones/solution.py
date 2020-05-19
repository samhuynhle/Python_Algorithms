# Leet Code's Arrays 101 first algorithm to get warmed up in doing algorithms again (05/19/2020)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        longest = 0
        
        # utilize for each loop rather than range loop due to slightly quicker
        # don't need to calculate the length of the array with len(nums)
        for num in nums:
            if num == 1 : count += 1
            else: 
                longest = max(count, longest)
                count = 0
        
        # need to do one more comparison in case nums end with a 1 and count is longer than longest
        return max(longest, count)