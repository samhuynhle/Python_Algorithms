class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        
        if len(nums)==len(hashset):
            return False
        else:
            return True