##array[1,2,3,5,7,4] and [[0,2] [2,3]]


def prefix_sum(array, arr):
    sum = 0
    val1 = []
    for i in range(len(array)):
        array[i] = sum + array[i]
        sum = array[i]

    for val in range(len(arr)):
        print (arr[val][0], arr[val][1])
        if arr[val][0] == 0:
            val1.append( array[arr[val][1]] - array[arr[val][0]] )
        else:
            val1.append( array[arr[val][1]] - array[arr[val][0] - 1] )
       
    return val1, array
# Test the function with an example
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    result = prefix_sum(arr, [[0, 2], [1, 3], [2, 4]])
    print(result)  # Output: [1, 3, 6, 10, 15]



#Given an array of integers nums and an integer k,
#  return the total number of subarrays whose sum equals to k.

#[2,3,5,4,6,7]
#[2,5,10,14,20,27]
    def subarraySum(nums, k):
        count = 0
        sum = 0
        prefix_sum = {0: 1}
       

        for i in range(len(nums)):
            nums[i] = sum + nums[i]
            sum = nums[i]
            print('sum:', sum, nums)
            print(prefix_sum)
            
            if sum - k in prefix_sum:
                print('here')
                count += prefix_sum[sum - k]
            if sum in prefix_sum:
                print('here1')
                prefix_sum[sum] += 1
            else:
                prefix_sum[sum] = 1
        return count
    
    # Test the function with an example
    if __name__ == "__main__":
        arr = [1, 2, 3, 4, 5]
        result = subarraySum(arr, 5)
        print(result)  # Output: [1, 3, 6, 10, 15]


#Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

#nums = [4,5,0,-2,-3,1], k = 5
#Output: 7
#Explanation: There are 7 subarrays with a sum divisible by k = 5:
#[4, 5, 0], [5, 0], [0], [-2, -3], [-3, 1], [4, 5, 0, -2, -3], and [5, 0, -2, -3, 1].
#nums = [5], k = 9
#Output: 0
#Explanation: There is no subarray with a sum divisible by k = 9.
        def subarraySum(nums, k):
            count = 0
            sum = 0
            prefix_sum = {0: 1}
            print ("check=======")

            for i in range(len(nums)):
                nums[i] = sum + nums[i]
                sum = nums[i]
                print('sum:', sum, nums, sum % k)
                print(prefix_sum)
                
                if sum % k in prefix_sum:
                    print('here')
                    count += prefix_sum[sum % k]
                if sum % k in prefix_sum:
                    print('here1')
                    prefix_sum[sum % k] += 1
                else:
                    prefix_sum[sum % k] = 1
            return count
        
        # Test the function with an example
        if __name__ == "__main__":
            arr = [1, 2, 3, 4, 5]
            result = subarraySum(arr, 5)
            print(result)



#Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
#A good subarray is a subarray where the sum of the elements is multiple of k and the length of the subarray is at least 2.

        def checkSubarraySum(nums, k):
            sum = 0
            prefix_sum = {0: -1}
            print ("check=======")
            for i in range(len(nums)):
                sum += nums[i]
                print('sum:', sum, nums, sum % k)
                if sum % k in prefix_sum:
                    if i - prefix_sum[sum % k] > 1:
                        return True
                else:
                    prefix_sum[sum % k] = i
            return False
        
        # Test the function with an example
        if __name__ == "__main__":
            arr = [1, 2, 3, 4, 5]
            result = checkSubarraySum(arr, 5)
            print(result)

    
#Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#The answer will be 0 if there is no subarray with equal number of 0 and 1.
#nums = [0,1], Output: 2
#nums = [0,1,0], Output: 2
#nums = [0,1,0,1], Output: 4
        def findMaxLength(nums):
            count = 0
            sum = 0
            prefix_sum = {0: -1}
            print ("check=======")
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = -1
                sum += nums[i]
                print('sum:', sum, nums, sum % k)
                if sum in prefix_sum:
                    count = max(count, i - prefix_sum[sum])
                else:
                    prefix_sum[sum] = i
            return count
