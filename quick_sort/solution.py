class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # return sorted(nums)
        
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def partition(self, alist, left, right):
        pivot = alist[right]
        start = left
        end = right - 1
        while start <= end:
            if alist[start] < pivot:
                start += 1
            elif alist[end] >= pivot:
                end -= 1
            else:
                alist[start], alist[end] = alist[end], alist[start]
                start += 1
                end -= 1
        alist[start], alist[right] = alist[right], alist[start]
        return start
    
    def quicksort(self, alist, left, right):
        if left >= right:
            return
        pivot = self.partition(alist, left, right)
        self.quicksort(alist, left, pivot-1)
        self.quicksort(alist, pivot+1, right)