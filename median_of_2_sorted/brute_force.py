def findMedianSortedArrays(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    nums3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            k = k + 1
            i = i + 1
        else:
            nums3[k] = nums2[j]
            k = k + 1
            j = j + 1
    while i < n1:
        nums3[k] = nums1[i]
        k = k + 1
        i = i + 1
    while j < n2:
        nums3[k] = nums2[j]
        k = k + 1
        j = j + 1
        
    if(len(nums3) % 2 == 1):
        x = len(nums3)/2
        return nums3[int(x)]
    else:
        x = (len(nums3) - 1)/2
        y = (len(nums3) + 1)/2
        return (nums3[int(x)] + nums3[int(y)])/2