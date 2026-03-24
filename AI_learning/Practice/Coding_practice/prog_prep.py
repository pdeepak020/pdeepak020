"""
DSA (Data Structures and Algorithms) Preparation Notes
=====================================================
This file covers all major DSA concepts and includes best interview questions on strings, arrays, lists, and dictionaries with examples and code.
"""

# 1. Data Structures Overview
# ---------------------------
# Data structures organize and store data efficiently. Common types:
# - Array
# - List
# - Dictionary (Hash Map)
# - Stack
# - Queue
# - Tree
# - Graph
# - Set

# 2. Algorithms Overview
# ----------------------
# Algorithms are step-by-step procedures for solving problems. Key types:
# - Searching (Linear, Binary)
# - Sorting (Bubble, Selection, Insertion, Merge, Quick)
# - Recursion
# - Dynamic Programming
# - Greedy Algorithms
# - Backtracking

# 3. String Interview Questions & Examples
# ----------------------------------------
# Q1: Reverse a string
s = "hello"
print(s[::-1])  # Output: 'olleh'

# Q2: Check if a string is a palindrome
s = "madam"
print(s == s[::-1])  # Output: True

# Q3: Count vowels in a string
s = "interview"
vowels = 'aeiouAEIOU'
print(sum(1 for c in s if c in vowels))  # Output: 4

# Q4: Find first non-repeating character
#s = "aabbcdeff"
s = [1,2,3,3,4,2,3,4,3]
from collections import Counter
counts = Counter(s)
for c in s:
    if counts[c] == 1:
        print(c)  # Output: 'c'
        break


# 4. Array Interview Questions & Examples
# ---------------------------------------
# Q1: Find the largest element
#    
def mass(arr):
    max_num = arr[0]
    for num in arr[1:]:
        if num > max_num:
            max_num = num
    return max_num

arr = [2,3,53,4,6,7,5]
print ('deep', mass(arr))
        

print(max(arr))  # Output: 9

# Q2: Remove duplicates
arr = [1, 2, 2, 3, 4, 4]
print(list(set(arr)))  # Output: [1, 2, 3, 4]

def dup(arr):
    a= 0
    for i in range(len(arr) - 1):
        if arr[a] == arr[a + 1]:
            arr.pop(a + 1)
        else:
            a +=1
           
    return arr

print ('dup', dup(arr))

# Q3: Find the missing number (1 to n)
arr = [1, 2, 4, 5]
n = 5
print(n*(n+1)//2 - sum(arr))  # Output: 3

# Q4: Rotate array by k steps
arr = [1,2,3,4,5]
k = 2
print(arr[-k:] , arr[:-k])
print(arr[-k:] + arr[:-k])  # Output: [4, 5, 1, 2, 3]

# 5. List Interview Questions & Examples
# --------------------------------------
# Q1: Merge two sorted lists
l1 = [1,3,5]
l2 = [2,4,6]
print(sorted(l1 + l2))  # Output: [1,2,3,4,5,6]

# Q2: Find intersection of two lists
l1 = [1,2,3]
l2 = [2,3,4]
print(list(set(l1).intersection(set(l2))))  # Output: [2, 3]

# Q3: Remove element by value
lst = [1,2,3,4]
lst.remove(3)
print(lst)  # Output: [1,2,4]

# Q4: Find all pairs with given sum
lst = [1,2,3,4,5]
target = 5
pairs = [(x, y) for i, x in enumerate(lst) for y in lst[i+1:] if x + y == target]
print(pairs)  # Output: [(1, 4), (2, 3)]

# 6. Dictionary Interview Questions & Examples
# --------------------------------------------
# Q1: Count frequency of elements
lst = [1,2,2,3,3,3]
from collections import Counter
print(dict(Counter(lst)))  # Output: {1: 1, 2: 2, 3: 3}

# Q2: Invert a dictionary
d = {'a': 1, 'b': 2}
print({v: k for k, v in d.items()})  # Output: {1: 'a', 2: 'b'}

# Q3: Merge two dictionaries
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Q4: Find key with max value
scores = {'Alice': 88, 'Bob': 95, 'Charlie': 90}
print(max(scores, key=scores.get))  # Output: 'Bob'

# 7. DSA Concepts Summary
# -----------------------
# - Arrays: Fixed size, fast access, used for contiguous data.
# - Lists: Dynamic size, easy insertion/deletion.
# - Dictionaries: Key-value pairs, fast lookup.
# - Strings: Immutable sequences of characters.
# - Stacks/Queues: LIFO/FIFO structures for order management.
# - Trees/Graphs: Hierarchical and networked data.
# - Sorting/Searching: Efficient data retrieval and organization.
# - Recursion: Function calling itself for problem breakdown.
# - Dynamic Programming: Breaking problems into subproblems, storing results.
# - Greedy: Making locally optimal choices.
# - Backtracking: Trying all possibilities recursively.

# 8. Detailed Algorithms Concepts, Examples, and Code
# ---------------------------------------------------

# 8.1 Searching Algorithms
# ------------------------
# Linear Search: Check each element one by one.
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
# Example:
arr = [2, 4, 6, 8, 10]
print(linear_search(arr, 8))  # Output: 3

# Binary Search: Efficient search in sorted array.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Example:
arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 5))  # Output: 2

# 8.2 Sorting Algorithms
# ----------------------
# Bubble Sort: Repeatedly swap adjacent elements if out of order.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Example:
arr = [5, 1, 4, 2, 8]
print(bubble_sort(arr))  # Output: [1, 2, 4, 5, 8]

# Selection Sort: Select minimum and swap with current position.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# Example:
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # Output: [11, 12, 22, 25, 64]

# Insertion Sort: Insert each element into its correct position.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Example:
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]

# Merge Sort: Divide and conquer, merge sorted halves.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
# Example:
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]

# Quick Sort: Partition and recursively sort subarrays.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Example:
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))  # Output: [1, 5, 7, 8, 9, 10]

# 8.3 Recursion
# -------------
# Function calling itself to solve subproblems.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Example:
print(factorial(5))  # Output: 120

# 8.4 Dynamic Programming
# -----------------------
# Store results of subproblems to avoid recomputation.
def fib_dp(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
# Example:
print(fib_dp(10))  # Output: 55

# 8.5 Greedy Algorithms
# ---------------------
# Make locally optimal choices at each step.
def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count
# Example:
coins = [1, 2, 5]
print(coin_change(coins, 11))  # Output: 3 (5+5+1)

# 8.6 Backtracking
# ----------------
# Try all possibilities recursively.
def solve_n_queens(n):
    solutions = []
    def backtrack(row, cols, diags1, diags2, state):
        if row == n:
            solutions.append(state[:])
            return
        for col in range(n):
            if col in cols or (row+col) in diags1 or (row-col) in diags2:
                continue
            cols.add(col)
            diags1.add(row+col)
            diags2.add(row-col)
            state.append(col)
            backtrack(row+1, cols, diags1, diags2, state)
            cols.remove(col)
            diags1.remove(row+col)
            diags2.remove(row-col)
            state.pop()
    backtrack(0, set(), set(), set(), [])
    return solutions
# Example:
print(solve_n_queens(4))  # Output: [[1, 3, 0, 2], [2, 0, 3, 1]]

# End of Detailed Algorithms Concepts
