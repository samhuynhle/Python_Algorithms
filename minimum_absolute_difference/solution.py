class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]: # function takes in an array of integers
        arr_sorted = sorted(arr) # we need to sort the array from min to max
        
        return_list = [] # initialize our return
        min_num = 10**6 # initialize a minimum number, set to large arbitrary number
        for i in range(len(arr_sorted) - 1): # loop through the array
            if (arr_sorted[i+1] -  arr_sorted[i]) < min_num: # two conditionals: first one is if we get a new minimum
                min_num = arr_sorted[i+1] - arr_sorted[i] # reset the minimum number
                return_list = [] # reset our return array as there is a new minimum
                return_list.append([arr_sorted[i],arr_sorted[i+1]]) # add the pair to the return array
            elif (arr_sorted[i+1] -  arr_sorted[i]) == min_num: # second conditation, the difference between the integers is equal to the minimum
                return_list.append([arr_sorted[i],arr_sorted[i+1]]) # just add it to our return array
        
        return return_list # return the array