#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, 
# nums1 has a length of m + n, where the first m elements denote the 
# elements that should be merged, and the last n elements are set to 0 and 
# should be ignored. nums2 has a length of n.
#You must solve the problem in-place in O(1) extra space complexity.
#Example 1:
#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]
#Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6], and there are no elements left behind.
#Example 2:
#Input: nums1 = [1], m = 1, nums2 = [], n = 0
def merge(nums1, m, nums2, n):
    p1 = 0
    p2 = 0
    for i in range(m + n):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            nums1.insert(p1, nums2[p2])
            p2 += 1
            p1 += 1
    return nums1

    # Test the function with an example
if __name__ == "__main__":
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        result = merge(nums1, m, nums2, n)
        print(result)  # Output: [1, 2, 2, 3, 5, 6]

#[2,7,11,15], target = 9
def sortedArray(arr, n):
        # Initialize two pointers
        a= 0
        b = 1
        for i in range(len(arr)):
             if arr[a] + arr[b] == target:
                return [a, b]
             else:
                b += 1
                if b == len(arr):
                    a += 1
                    b = a + 1
        return [-1, -1]  # Return -1 if no such indices are found

    # Test the function with an example
if __name__ == "__main__":
        arr = [2, 2, 11, 15]
        target = 9
        result = sortedArray(arr, target)
        print(result)  # Output: [0, 1]


            



        

 
       
