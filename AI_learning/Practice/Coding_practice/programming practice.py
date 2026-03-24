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
    while p1 <= m +n:
        if nums1[p1] < nums2[p2]:
            if p1 > m:
                nums1[p1] = nums2[p2]
                if p2 == n:
                    break
                else:
                    p2 +=1
            p1 += 1
        else:
            nums1.insert(p1, nums2[p2])
            p2 += 1
            p1 += 1
    return nums1

    # Test the function with an example
    #example - 
if __name__ == "__main__":
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        result = merge(nums1, m, nums2, n)
        print('echk - ', result)  # Output: [1, 2, 2, 3, 5, 6]

#[1,15,11,7], target = 9
def sortedArray(arr, n):
        # Initialize two pointers
        a= 0
        b = 1
        while a <= len(arr):
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
        arr = [15, 2, 11, 7]
        target = 9
        result = sortedArray(arr, target)
        print(result)  # Output: [0, 1]


#find the duplicate in array and true if found else return false
import sys
def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
#time complexity: O(n)
#space complexity: O(n)


#find if the given strings are anagram if yes retrun true else return false using array
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    # Create a count array for characters
    # Assuming ASCII characters, we can use a fixed-size array
    count = [0] * 256  # Assuming ASCII characters
    # Count occurrences of each character in both strings
    for char in str1:
        count[ord(char)] += 1
    for char in str2:
        count[ord(char)] -= 1
    return all(x == 0 for x in count)
def main():
    str1 = "listen"
    str2 = "silent"
    print ('check',sorted(str1), sorted(str2))
    if is_anagram(str1, str2):
        print(f"{str1} and {str2} are anagrams.")
    else:
        print(f"{str1} and {str2} are not anagrams.")

main()

def is_anagram_two_pointer(str1, str2):
    # If lengths differ, not anagrams
    if len(str1) != len(str2):
        return False
    # Sort both strings
    s1 = sorted(str1)
    s2 = sorted(str2)
    # Use two pointers to compare
    left, right = 0, len(s1) - 1
    while left <= right:
        if s1[left] != s2[left] or s1[right] != s2[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"
    print(is_anagram_two_pointer(str1, str2))  # Output: True




#find the group of anagrams in the given list of strings
def group_anagrams(strs):
    anagrams = {}
    
    for s in strs:
        # Sort the string to create a key
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    
    return list(anagrams.values())

# Example usage
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    print("Grouped Anagrams:", result)


            
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call
# Example usage:
result = factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
print("Factorial of 5:", result)  # Output: Factorial of 5

#factorial -




        

 
       
