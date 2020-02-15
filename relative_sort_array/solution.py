class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        left = 0
        
        for i in arr2:
            left = self.relativeSort(arr1, i, left)
        
        self.quickSort(arr1, left, len(arr1) - 1)
        # arr1[left:] = sorted(arr1[left:])
        
        return arr1
    
    def relativeSort(self, arr1, target, left):
        right = len(arr1) - 1
        
        while(left < right):
            while(arr1[left] == target):
                left += 1
            while(arr1[right] != target):
                right -= 1
            if left < right:
                arr1[left], arr1[right] = arr1[right], arr1[left]
            
        return left
    
    def quickSort(self, arr1, left, right):
        left  = left
        right = right
        
        if left < right:
            pi = self.partition(arr1, left, right)
            
            self.quickSort(arr1, left, pi-1)
            self.quickSort(arr1, pi+1, right)
            
    
    def partition(self,arr,left,right):
        index = left - 1
        pivot = arr[right]

        for j in range(left , right):
            if   arr[j] <= pivot: 
                index = index+1 
                arr[index],arr[j] = arr[j],arr[index] 

        arr[index+1],arr[right] = arr[right],arr[index+1] 
        return index + 1 