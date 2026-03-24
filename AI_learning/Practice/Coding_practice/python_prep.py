#numpy - numerical python
#pandas - data handaling
#matplot seaborn - visualization libraries
#scipy - scientific python
#stats model - statistical model
#scikit learn- data preprocessing, base for machine learning, for large data

#In Python, imports are used to bring in modules that provide extra #functionality. Here are some common imports and their uses:

# sys: Provides access to system-specific parameters and functions.
# Example uses: sys.argv for command-line arguments, sys.exit() to exit a program.

# os: Provides functions to interact with the operating system.
# Example uses: os.listdir() to list files in a directory, os.path for file path operations, os.environ for environment variables.

# math: Provides mathematical functions like math.sqrt(), math.pi, etc.

# random: Used for generating random numbers, shuffling, and sampling.

# datetime: For working with dates and times.

# json: For working with JSON data (parsing and writing).

# re: For regular expressions (pattern matching in strings).

# Summary:

# sys is for system-level operations.
# os is for interacting with the operating system (files, directories, environment).
# Other modules like math, random, datetime, json, and re provide specialized utilities for math, randomness, date/time, data formats, and text processing.

import sys
import os
import math
import random
import datetime
import json
from turtle import pd

from numpy import percentile

#use of above imports
#sys.exit("Exiting the program")
print("Current working directory:", os.getcwd())    
print("Square root of 16:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))
print("Current date and time:", datetime.datetime.now())    



#A decorator in Python is a special function that modifies the 
# behavior of another function or method. Decorators are often
#  used to add extra functionality (like logging, authentication, 
# or timing) to existing functions without changing their code.

# How it works:
# A decorator is applied to a function using the @decorator_name
#  syntax above the function definition.
# Example usage
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# --- More Detailed Examples of Decorator Functions ---

# 1. Logging Decorator: Logs function calls and arguments
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)  # Output: logs the call and result

# 2. Timing Decorator: Measures execution time of a function
import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    print("Function finished sleeping.")

slow_function()  # Output: prints execution time

# 3. Parameterized Decorator: Decorator that takes arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Repeat {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")  # Output: prints greeting 3 times

# The line if __name__ == "__main__": in Python is used to check whether 
# the script is being run directly or being imported as a module in
#  another script.

# If the script is run directly (e.g., python myscript.py), __name__ is 
# set to "__main__", so the code inside this block will execute.
# If the script is imported into another script, __name__ will be 
# set to the module's name, and the code inside this block will not run.
# Purpose:
# It allows you to write code that can be used both as a reusable
#  module and as a standalone program with test or demo code at the bottom.
if __name__ == "__main__":
    say_hello("Alice")


# In Python, an iterator is an object that allows you to traverse through all
#  the elements of a collection (like a list or tuple), one element at a time.
#  Iterators implement two methods: iter() and next().

# The iter() method returns the iterator object itself.
# The next() method returns the next value from the collection. When there are
#  no more items, it raises a StopIteration exception
# Creating an iterator from a list
my_list = [1, 2, 3]
my_iter = iter(my_list)  # Get an iterator object

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
# next(my_iter) would raise StopIteration
# Example usage of the iterator
for num in my_iter:
    print(num)  # This will not print anything since the iterator is exhausted

# A generator is a special type of iterator in Python that allows you to
#  create iterators in a more concise way using the yield statement.
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i  # Yielding a value instead of returning it 
# Example usage of the generator
for num in generate_numbers(5):
    print(num)  # Output: 1, 2, 3, 4, 5

# The yield statement allows the function to return a value and pause its state,
# so it can be resumed later. 
def simple_gen():
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")

gen = simple_gen()
print(next(gen))  # Output: Start \n 1
print(next(gen))  # Output: After first yield \n 2
# If you call next(gen) again, it will print "After second yield" and raise StopIteration
# This makes generators memory-efficient for large datasets.


# A context manager in Python is a construct that allows you to set up and clean
# up resources automatically. It is most commonly used with the with statement,
#  which ensures that resources like files or network connections are properly 
#  acquired and released, even if errors occur.

# The most common example is opening a file:
#with open('example.txt', 'r') as file:
 #    data = file.read()
# # The file is automatically closed when the block ends, even if an error occurs.
# How it works:

# The context manager implements two methods: enter() (setup) and exit() (cleanup).
# When you enter the with block, enter() is called.
# When you exit the block, exit() is called, even if an exception occurs.
#custom context manager example
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # Return an object to use inside the with block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True  # Suppress exceptions if needed

with MyContextManager() as cm:
    print("Inside the context")
    # You can raise an exception here to see how it is handled
    # raise ValueError("An example error")



# In Python, defining a method with def name in a class (for example, def __init__,
#  def __str__, def __len__, etc.) means you are creating a special method, also called 
# a "dunder" (double underscore) or magic method.

# These methods have special meaning and are used by Python to perform certain 
# operations automatically. For example:

# def __init__(self, ...): is called when you create a new object (the constructor).
# def __str__(self): is called when you use str() or print() on the object.
# def __len__(self): is called when you use len() on the object.
# These methods let you define how your class behaves with built-in functions and 
# operators. They are not meant to be called directly; Python calls them for you 
# in specific situations.


# Multiprocessing in Python allows you to run multiple processes in parallel
# , making use of multiple CPU cores. This is especially useful for CPU-bound
#  tasks, such as heavy computations, where threading is limited by the Global
#  Interpreter Lock (GIL).

The GIL (Global Interpreter Lock) is a mutex (lock) used in the standard CPython implementation of Python. It ensures that only one thread executes Python bytecode at a time, even on multi-core processors.

Why does it exist?

It simplifies memory management in CPython by preventing race conditions.
It makes CPython easier to implement and maintain.
Implications:

Multithreading: True parallel execution of threads is not possible for CPU-bound tasks in CPython. Only one thread runs Python code at a time.
I/O-bound tasks: Threads can still be useful for I/O-bound operations, as the GIL is released during I/O (e.g., file, network).
Multiprocessing: For CPU-bound parallelism, use the multiprocessing module, which runs separate processes (each with its own GIL).
Summary:
The GIL is a limitation for multi-threaded, CPU-bound Python programs in CPython, but not for I/O-bound tasks or when using multiprocessing.

# Here's a simple example using the multiprocessing module to calculate the
#  square of numbers in parallel:

import multiprocessing

def square(n):
    print(f"Square of {n}: {n * n}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=square, args=(num,))
        processes.append(p)
        p.start()  # Start the process

    for p in processes:
        p.join()  # Wait for all processes to finish
# This code creates a separate process for each number in the list,
# calculates its square, and prints the result. Each process runs independently,
# allowing for parallel execution on multiple CPU cores.
#joining the processes ensures that the main program waits for all processes to complete before exiting.



# Multithreading in Python allows you to run multiple threads 
# (smaller units of a process) concurrently within a single process.
#  Threads share the same memory space, making it easy to share data,
#  but they are limited by the Global Interpreter Lock (GIL), so true
#  parallelism is only achieved for I/O-bound tasks (like file or network
#  operations), not CPU-bound tasks.

# Example 1: Simple threading with the threading module
import threading
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
if __name__ == "__main__":
    thread = threading.Thread(target=print_numbers, n)
    thread.start()  # Start the thread
    thread.join()   # Wait for the thread to finish
# Example 2: Using a thread pool for concurrent execution
from concurrent.futures import ThreadPoolExecutor
def square(n):
    return n * n
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square, numbers))
    print("Squares:", results)
# Example 3: Using a thread pool for concurrent execution
# This code creates a thread pool with a maximum of 3 worker threads,
# allowing it to execute the square function concurrently for each number in the list.


#list comprehension is a concise way to create lists in Python.
# It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range).
# Example: Create a list of squares of numbers from 0 to 9
squares = [x * x for x in range(10)]
print("Squares:", squares)  # Output: Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# List comprehension can also include conditions to filter items.
# Example: Create a list of even squares from 0 to 9
even_squares = [x * x for x in range(10) if x % 2 == 0]
print("Even Squares:", even_squares)  # Output: Even Squares: [0, 4, 16, 36, 64]
# List comprehension is often more readable and concise than using traditional loops for creating lists.

#in comprehension intead ofr square[] bracets use () for generator
# Example: Create a generator of squares of numbers from 0 to 9
squares_gen = (x * x for x in range(10))
print("Squares Generator:")
for square in squares_gen:
    print(square)  # Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81


#difference between sort and sorted funstions 
# The sort() method sorts a list in place and returns None.
# It modifies the original list.
# Example:
my_list = [3, 1, 4, 2]
my_list.sort()  # Sorts the list in place
print("Sorted list using sort():", my_list)  # Output: [1, 2, 3, 4]
# The sorted() function returns a new sorted list from the elements of any iterable.
# It does not modify the original iterable.
def sorted_list(iterable):
    return sorted(iterable)  # Returns a new sorted list
# Example:
original_list = [3, 1, 4, 2]
sorted_result = sorted_list(original_list)
print("Original list:", original_list)  # Output: [3, 1, 4, 2]
print("Sorted list using sorted():", sorted_result)  # Output: [1, 2, 3, 4]
# The sorted() function can also take a key function and reverse flag.
# Example: Sort a list of tuples by the second element
def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])  # Sort by second element
# Example:
tuples = [(1, 3), (2, 1), (3, 2)]
sorted_tuples = sort_tuples(tuples)
print("Sorted tuples by second element:", sorted_tuples)  # Output: [(2, 1), (3, 2), (1, 3)]

#sort can not be used for immutable types like strings or tuples, while sorted can be used on any iterable.

#filter function in Python is used to filter elements from an iterable (like a list or tuple) based on a specified condition.
# It takes two arguments: a function that defines the condition and the iterable to filter.
# Example: Filter even numbers from a list
def is_even(n):
    return n % 2 == 0
def filter_even_numbers(numbers):
    return list(filter(is_even, numbers))  # Returns a list of even numbers
# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter_even_numbers(numbers)
print("Even numbers:", even_numbers)  # Output: [2, 4, 6]

# The filter function can also be used with lambda functions for concise filtering.
def filter_even_numbers_lambda(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers))  # Using lambda function
# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers_lambda = filter_even_numbers_lambda(numbers)
print("Even numbers using lambda:", even_numbers_lambda)  # Output: [2, 4, 6]
# The filter function returns an iterator, so you can convert it to a list or use it directly in a loop.
# In Python, the map function is used to apply a given function to each item in an iterable (like a list or tuple).
# It takes two arguments: a function and an iterable, and returns an iterator that produces the results.
# Example: Square each number in a list
def square(n):
    return n * n
def map_square(numbers):
    return list(map(square, numbers))  # Returns a list of squared numbers
# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map_square(numbers)
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]
# The map function can also be used with lambda functions for concise mapping.
def map_square_lambda(numbers):
    return list(map(lambda n: n * n, numbers))  # Using lambda function
# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers_lambda = map_square_lambda(numbers)
print("Squared numbers using lambda:", squared_numbers_lambda)  # Output: [1, 4, 9, 16, 25]
# The map function returns an iterator, so you can convert it to a list or use it directly in a loop.
# In Python, the zip function is used to combine multiple iterables (like lists or tuples) into a single iterable of tuples.
# It pairs elements from each iterable based on their positions.
def zip_lists(list1, list2):
    return list(zip(list1, list2))  # Returns a list of tuples
# Example usage:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip_lists(list1, list2)
print("Zipped lists:", zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# If the iterables are of different lengths, zip stops at the shortest one.
def zip_lists_diff_length(list1, list2):
    return list(zip(list1, list2))  # Returns a list of tuples
# Example usage:
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
zipped_diff_length = zip_lists_diff_length(list1, list2)
print("Zipped lists with different lengths:", zipped_diff_length)  # Output: [(1, 'a'), (2, 'b')]
# You can also use zip with more than two iterables.
def zip_multiple_lists(*lists):
    return list(zip(*lists))  # Returns a list of tuples
# Example usage:
lists = [[1, 2, 3], ['a', 'b', 'c'], [True, False, True]]
zipped_multiple = zip_multiple_lists(*lists)
print("Zipped multiple lists:", zipped_multiple)  # Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# In Python, the enumerate function is used to iterate over an iterable (like a list or tuple) while keeping track of the index of each element.
# It returns an iterator that produces pairs of index and value.
def enumerate_list(my_list):
    return list(enumerate(my_list))  # Returns a list of tuples (index, value)
# Example usage:
my_list = ['a', 'b', 'c']
enumerated = enumerate_list(my_list)
print("Enumerated list:", enumerated)  # Output: [(0, 'a'), (1, 'b'), (2, 'c')]
# You can also specify a starting index by passing a second argument to enumerate.
def enumerate_list_start(my_list, start=0):
    return list(enumerate(my_list, start))  # Returns a list of tuples (index, value)
# Example usage:
my_list = ['a', 'b', 'c']
enumerated_start = enumerate_list_start(my_list, start=1) 
print("Enumerated list with start index:", enumerated_start)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# Enumerate is often used in loops to get both the index and value of each element.
#example usage:
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: a
# Index: 1, Value: b
# Index: 2, Value: c

#lambda function declaration in Python is a way to create small, anonymous functions.
# It is often used for short, throwaway functions that are not needed elsewhere in the code.
# The syntax for a lambda function is:
# lambda arguments: expression
# Example: A simple lambda function that adds two numbers
add = lambda x, y: x + y
# Example usage:
result = add(3, 5)  # Calls the lambda function with arguments 3 and 5
print("Result of addition:", result)  # Output: Result of addition: 8



#classes in Python are used to create user-defined data types that encapsulate data and behavior.
# A class is defined using the class keyword, followed by the class name and a colon.
# Example: Defining a simple class
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def bark(self):
        print(f"{self.name} says Woof!")
# Example usage:
my_dog = Dog("Buddy", 3)  # Creating an instance of the Dog
my_dog.bark()  # Output: Buddy says Woof!
# Inheritance allows you to create a new class that inherits attributes and methods from an existing class.
# Example: Inheriting from the Dog class
class Puppy(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call the parent class constructor
        self.breed = breed  # New instance variable

    def play(self):
        print(f"{self.name} is playing!")
# Example usage:
my_puppy = Puppy("Charlie", 1, "Labrador")  # Creating an instance of the Puppy
my_puppy.bark()  # Output: Charlie says Woof!
my_puppy.play()  # Output: Charlie is playing!

#recursion in Python is a programming technique where a function calls itself to solve a problem.
# It is often used to break down complex problems into simpler subproblems.
# A recursive function must have a base case to stop the recursion and prevent infinite loops.
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call
# Example usage:
result = factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
print("Factorial of 5:", result)  # Output: Factorial of 5
# Recursion can also be used for problems like Fibonacci sequence, tree traversal, etc.
# 2. Fibonacci sequence (nth term)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci(6):", fibonacci(6))  # Output: 8

def fibonacci_sequence(n):
    """Return a list containing the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# 3. Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print("Reverse of 'hello':", reverse_string("hello"))  # Output: 'olleh'


# 5. Check if a number is a palindrome (using recursion)
def is_palindrome(num, temp=None):
    if temp is None:
        temp = num
    if num == 0:
        return 0
    rev = is_palindrome(num // 10, temp)
    rev = rev * 10 + num % 10
    if num == temp and rev == temp:
        return True
    elif num == temp:
        return False
    return rev
print("Is 121 a palindrome?", is_palindrome(121))  # Output: True

# 6. Recursively print elements of a list
def print_list(lst):
    if not lst:
        return
    print(lst[0])
    print_list(lst[1:])
print("Printing list recursively:")
print_list([10, 20, 30, 40])

# 8. Find the maximum element in a list recursively
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))
print("Max in [1, 5, 3, 9, 2]:", find_max([1, 5, 3, 9, 2]))  # Output: 9

# 9. Recursively flatten a nested list
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print("Flattened list:", flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]

# 10. Recursively count digits in a number
def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)
print("Number of digits in 12345:", count_digits(12345))  # Output: 5


x= 45.77
y= x
print (f" {id(x)}, {id(y)}")  # Output: id of x and y will be the same
#print using f string formatting

# In Python, the id() function returns the identity of an object, which is a unique
#  integer that represents the object's memory address.
# The id of an object remains constant during its lifetime.

a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
print('a is b' , a is b) #gives bool value True
print('a is not b' , a is not b) #gives bool value False

#string functions
# In Python, strings are immutable sequences of characters, and they come with a variety of built-in methods for manipulation.
# Here are some common string functions and their uses:
def string_functions_example():
    my_string = "Hello, World!"

    #example to show string in immutable
    print("Original string:", my_string)  # Output: Hello, World!
    # Demonstrating string immutability
    # Attempting to change a character in the string will raise an error
    # my_string[0] = 'h'  # Uncommenting this line will raise a TypeError
   

    # 1. len() - Returns the length of the string
    print("Length of string:", len(my_string))  # Output: 13

    # 2. str.lower() - Converts the string to lowercase
    print("Lowercase:", my_string.lower())  # Output: hello, world!

    # 3. str.upper() - Converts the string to uppercase
    print("Uppercase:", my_string.upper())  # Output: HELLO, WORLD!

    # 4. str.strip() - Removes leading and trailing whitespace
    print("Stripped:", "   Hello   ".strip())  # Output: Hello

    # 5. str.split() - Splits the string into a list of substrings
    print("Split:", my_string.split(", "))  # Output: ['Hello', 'World!']

    # 6. str.join() - Joins a list of strings into a single string
    print("Joined:", ", ".join(['Hello', 'World']))  # Output: Hello, World

    # 7. str.replace() - Replaces occurrences of a substring with another substring
    print("Replaced:", my_string.replace("World", "Python"))  # Output: Hello, Python!

# 8. str.find() - Returns the index of the first occurrence of a substring
    print("Index of 'World':", my_string.find("World"))  # Output: 7
# 9. str.count() - Counts the occurrences of a substring
    print("Count of 'o':", my_string.count("o"))  # Output: 2
# 10. str.startswith() - Checks if the string starts with a specified substring
    print("Starts with 'Hello':", my_string.startswith("Hello"))  # Output: True
# 11. str.endswith() - Checks if the string ends with a specified substring
    print("Ends with 'World!':", my_string.endswith("World!"))  #   
# Output: True
# 12. str.capitalize() - Capitalizes the first character of the string
    print("Capitalized:", my_string.capitalize())  # Output: Hello, world!
# 13. str.title() - Capitalizes the first character of each word in the string
    print("Title case:", my_string.title())  # Output: Hello, World!
# 14. str.isalpha() - Checks if all characters in the string are alphabetic
    print("Is alphabetic:", my_string.isalpha())  # Output: False (because of punctuation and space)
# 15. str.isdigit() - Checks if all characters in the string are digits
    print("Is digit:", "12345".isdigit())  # Output: True   
# 16. str.isalnum() - Checks if all characters in the string are alphanumeric
    print("Is alphanumeric:", "Hello123".isalnum())  # Output: True
# 17. str.islower() - Checks if all characters in the string are lowercase
    print("Is lowercase:", my_string.islower())  # Output: False
# 18. str.isupper() - Checks if all characters in the string are uppercase  
    print("Is uppercase:", my_string.isupper())  # Output: False
#calling the string functions example function
string_functions_example()


#file handaling in Python involves reading from and writing to files.
# Here are some common file handling operations:
# def file_handling_example():
#     # 1. Opening a file
#     with open('example.txt', 'w') as file:  # 'w' mode for writing
#         file.write("Hello, World!\n")  # Writing to the file

#     # 2. Reading from a file
#     with open('example.txt', 'r') as file:  # 'r' mode for reading
#         content = file.read()  # Read the entire file content
#         print("File content:", content)  # Output: Hello, World!

#     # 3. Appending to a file
#     with open('example.txt', 'a') as file:  # 'a' mode for appending
#         file.write("Appending new line.\n")  # Append to the file

#     # 4. Reading lines from a file
#     with open('example.txt', 'r') as file:
#         lines = file.readlines()  # Read all lines into a list
#         print("Lines in the file:", lines)  # Output: ['Hello, World!\n', 'Appending new line.\n']

#error handling in Python is done using try-except blocks.
# It allows you to catch and handle exceptions that may occur during program execution.
import os

def error_handling_example():
    try:
        # Attempt to open a file that may not exist
        # Check if the file exists
        if os.path.exists('deepak.txt'):
            with open('deepak.txt', 'r') as dp:
                   content = dp.read()
            print("File content:", content)
        else:

            print("File does not exist. Please check the file path.")
    except FileNotFoundError as e:
        print("Error:", e)    
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Execution completed, whether an error occurred or not.") 
#calling the error handling example function
error_handling_example()

#loops in Python are used to iterate over a sequence (like a list, tuple, or string) or to repeat a block of code multiple times.
# There are two main types of loops in Python: for loops and while loops.
# 1. For Loop: Used to iterate over a sequence (like a list, tuple, or string).
def for_loop_example():
    my_list = [1, 2, 3, 4, 5]
    print("For loop output:")
    for item in my_list:
        print(item)  # Output: 1, 2, 3, 4, 5

    #for loop with else
    for i in range(5):
# Prompt the user to enter their nationality
        food = input('Enter edible item :')
        if food == 'spam':
            print('No more spam please !!')
            break
        print('Great Delicious ')
    else : # This else block executes if the loop completes without hitting a break
        # Print a thank you message regardless
        print('I am so glad !! No Spam')
        print('Finally finshed stuffing myself!!')
    
    #for loop on string
    my_string = "Hello"
    print("For loop on string:")
    for char in my_string:
        print(char)  # Output: H, e, l, l, o
    #for loop with range
    print("For loop with range:")
    for i in range(5):  # Iterates from 0 to 4
        print(i)  # Output: 0, 1, 2, 3, 4
    #for with xrange
    #note: xrange is not available in Python 3, use range instead
    print("For loop with range and step:")
    for i in range(0, 10, 2):  # Iterates from 0 to 8 with a step of 2
        print(i)  # Output: 0, 2, 4, 6, 8
    #for loop on dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("For loop on dictionary:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")  # Output: Key-Value pairs of the dictionary
    # Output: Key: a, Value: 1, Key: b, Value: 2, Key: c, Value: 3
    #for loop for keys in dictionary
    print("For loop for keys in dictionary:")
    for key in my_dict.keys():
        print("Key:", key)  # Output: a, b, c


# 2. While Loop: Repeats a block of code as long as a specified condition is true.
def while_loop_example():
    count = 0
    print("While loop output:")
    while count < 5:  # Loop until count is less than 5
        print(count)  # Output: 0, 1, 2, 3, 4
        count += 1  # Increment count by 1
    #while loop with break and continue
    print("While loop with break and continue:")
    count = 0
    while True:  # Infinite loop
        if count == 3:
            print("Breaking the loop at count =", count)
            break  # Exit the loop when count is 3
        if count % 2 == 0:
            print("Skipping even count:", count)
            count += 1
            continue  # Skip the rest of the loop for even counts
        #pass in while loop
        if count % 2 != 0:
            print("Odd count:", count)
            count += 1
            pass ## Continue to the next iteration for odd counts
        
        print("Odd count:", count)  # Output: Odd counts only
        count += 1
        #pass in while loop
    print("While loop completed.")


# alpha to numeric
letter = 'a'
number = ord(letter.upper()) - ord('A') + 1
print(  ord(letter.upper()), ord('A'), number)  # Output: 1 , #for B outpu is 2, for C output is 3, and so on

# Define the function 'total' which takes a variable number of non-keyword arguments
def total(*args):
    # Initialize a variable 'tot' to store the total
    tot = 0
    # Iterate over the arguments and add each to 'tot'
    for n in args:
        tot += n
    # Print the total
    print(tot)

# Call the 'total' function with two arguments: 23 and 67 passed as a tuple
total(23, 67)
total(90, 100, 10, 30, 40)


# Define the function 'information' which takes a variable number of keyword arguments
def information(**kwargs):
    # Iterate over the keyword arguments and print each key-value pair
    for key, value in kwargs.items():
        print(key, ":", value)

# Call the 'information' function with 'name' and 'age' as keyword arguments
information(name = 'John Davis', age = 34)

# Print a list of all built-in functions and variables
print(dir(__builtins__))
# The dir() function returns a list of names in the current local scope or the attributes of an object.
# The __builtins__ module contains built-in functions, exceptions, and other objects that are always available in Python.
# The dir(__builtins__) will show you all the built-in functions and variables available in Python.
# The __name__ variable in Python is a special built-in variable that represents the name of the current module.
# If the module is being run as the main program, __name__ will be set to "__main__".
# If the module is being imported into another module, __name__ will be set to the module's name.
# Example usage:
if __name__ == "__main__":
    print("This script is being run directly.")
else:
    print("This script is being imported as a module.")
# The __name__ variable is often used to control the execution of code in a module.

# The __doc__ variable in Python is a special built-in variable that contains the documentation string (docstring) of a module, class, method, or function.
# It provides a way to access the documentation of an object programmatically.

# Import the 'reduce' function from 'functools'
from _functools import reduce
# Define a list of numbers
numbers = [2,4,6,8,10,12]
# Use the 'reduce' function with a lambda function to calculate the total sum
result = reduce(lambda x , y : x + y, numbers)
# Print the total sum
print('Total = ', result)


#sequencial datatypes in Python are ordered collections of items that can be accessed by their index.
# The most common sequential data types in Python are:
# 1. List: A mutable, ordered collection of items, heterogeneous in nature, duplicate values allowed.
def list_example():
    my_list = [1, 2, 3, 4, 5]
    print("List:", my_list)  # Output: [1, 2, 3, 4, 5]
    # Lists can contain different data types
    mixed_list = [1, "Hello", 3.14, True]
    print("Mixed List:", mixed_list)  # Output: [1, 'Hello', 3.14, True]
    # Lists are mutable (can be modified)
    my_list.append(6)  # Add an item to the end of the list
    print("List after append:", my_list)  # Output: [1, 2, 3, 4, 5, 6]
    my_list[0] = 10  # Change the first item
    print("List after modification:", my_list)  # Output: [10, 2, 3, 4, 5, 6]
    #list sclicing
    print("Sliced List:", my_list[1:4])  # Output: [2, 3, 4]
    print("Sliced List with step:", my_list[::2])  # Output: [10, 3, 5]
    print("Reversed List:", my_list[::-1])  # Output: [6, 5, 4, 3, 2, 10]
    #different methods for list
    my_list.remove(3)  # Remove an item by value
    print("List after removal:", my_list)  # Output: [10, 2, 4, 5, 6]
    my_list.sort()  # Sort the list in ascending order
    print("Sorted List:", my_list)  # Output: [2, 4, 5, 6, 10]
    my_list.reverse()  # Reverse the order of the list
    print("Reversed List:", my_list)  # Output: [10, 6, 5, 4, 2]
    my_list.extend([7, 8])  # Extend the list with another list
    print("List after extend:", my_list)  # Output: [10, 6, 5, 4, 2, 7, 8]
    my_list.insert(1, 20)  # Insert an item at a specific index
    print("List after insert:", my_list)  # Output: [10, 20, 6, 5, 4, 2, 7, 8]
    my_list.pop()  # Remove and return the last item
    print("List after pop:", my_list)  # Output: [10, 20, 6, 5, 4, 2, 7]
    my_list.index(20)  # Get the index of an item
    print("Index of 20:", my_list.index(20))  # Output: 1
    my_list.count(6)  # Count occurrences of an item
    print("Count of 6:", my_list.count(6))  # Output: 1

# 2. Tuple: An immutable, ordered collection of items, heterogeneous in nature, duplicate values allowed.
def tuple_example():
    my_tuple = (1, 2, 3, 4, 5)
    print("Tuple:", my_tuple)  # Output: (1, 2, 3, 4, 5)
    # Tuples can contain different data types
    mixed_tuple = (1, "Hello", 3.14, True)
    print("Mixed Tuple:", mixed_tuple)  # Output: (1, 'Hello', 3.14, True)
    # Tuples are immutable (cannot be modified)
    # my_tuple[0] = 10  # Uncommenting this line will raise a TypeError
    print("Tuple remains unchanged:", my_tuple)  # Output: (1, 2, 3, 4, 5)
    # Tuples can be used for unpacking
    a, b, c = my_tuple[:3]
    print("Unpacked values:", a, b, c)  # Output: Unpacked values: 1 2 3
    #tuple methods
    print("Length of tuple:", len(my_tuple))  # Output: 5
    print("Index of 3 in tuple:", my_tuple.index(3))  # Output: 2
    print("Count of 2 in tuple:", my_tuple.count(2))  # Output: 1
    print("Concatenated tuple:", my_tuple + (6, 7))  # Output: (1, 2, 3, 4, 5, 6, 7)

# 3. String: An immutable, ordered collection of characters, homogeneous in nature (all characters).
def string_example():
    my_string = "Hello, World!"
    print("String:", my_string)  # Output: Hello, World!
    # Strings are immutable (cannot be modified)
    # my_string[0] = 'h'  # Uncommenting this line will raise a TypeError
    print("String remains unchanged:", my_string)  # Output: Hello, World!
    # Strings can be sliced
    print("Sliced string:", my_string[0:5])  # Output: Hello
    # String methods
    print("Length of string:", len(my_string))  # Output: 13
    print("Uppercase string:", my_string.upper())  # Output: HELLO, WORLD!
    print("Lowercase string:", my_string.lower())  # Output: hello, world!
    print("Replaced string:", my_string.replace("World", "Python"))  # Output: Hello, Python!
    print("Split string:", my_string.split(", "))  # Output: ['Hello', 'World!']
    print("Count of 'o' in string:", my_string.count('o'))  # Output: 2
    print("Index of 'W' in string:", my_string.index('W'))  # Output: 7
    print("Concatenated string:", my_string + " How are you?")  # Output: Hello, World! How are you?
    print("Reversed string:", my_string[::-1])  # Output: !dlroW ,olleH
    print("String starts with 'Hello':", my_string.startswith("Hello"))  # Output: True
    print("String ends with '!':", my_string.endswith("!"))  # Output: True

# 4. Set: An unordered collection of unique items, heterogeneous in nature, no duplicate values allowed, mutable.
def set_example():
    my_set = {1, 2, 3, 4, 5}
    print("Set:", my_set)  # Output: {1, 2, 3, 4, 5}
    # Sets can contain different data types
    mixed_set = {1, "Hello", 3.14, True}
    print("Mixed Set:", mixed_set)  # Output: {1, 'Hello', 3.14}
    # Sets are unordered and do not allow duplicate values
    my_set.add(6)  # Add an item to the set
    print("Set after add:", my_set)  # Output: {1, 2, 3, 4, 5, 6}
    my_set.remove(3)  # Remove an item from the set
    print("Set after remove:", my_set)  # Output: {1, 2, 4, 5, 6}
    print("Length of set:", len(my_set))  # Output: 5
    print("Set union:", my_set.union({7, 8}))  # Output: {1, 2, 4, 5, 6, 7, 8}
    print("Set intersection:", my_set.intersection({4, 5}))  # Output: {4, 5}
    print("Set difference:", my_set.difference({2, 4}))  # Output: {1, 5, 6}
    print("Set symmetric difference:", my_set.symmetric_difference({2, 3, 4}))  # Output: {1, 5, 6, 2, 3}
    print("Is 2 in set?", 2 in my_set)  # Output: True
# 5. Dictionary: An unordered collection of key-value pairs, heterogeneous in nature, keys must be unique.
def dict_example():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Dictionary:", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
    # Dictionaries can contain different data types for keys and values
    mixed_dict = {1: "Hello", "key": 3.14, True: [1, 2, 3]}
    print("Mixed Dictionary:", mixed_dict)  # Output: {1: 'Hello', 'key': 3.14, True: [1, 2, 3]}
    # Accessing values by keys
    print("Value for key 'a':", my_dict['a'])  # Output: 1
    # Adding a new key-value pair
    my_dict['d'] = 4
    print("Dictionary after adding a new key:", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # Modifying an existing value
    my_dict['b'] = 5
    print("Dictionary after modifying a value:", my_dict)  # Output: {'a': 1, 'b': 5, 'c': 3, 'd': 4}
    # Removing a key-value pair
    del my_dict['c']
    print("Dictionary after removing a key:", my_dict)  # Output: {'a': 1, 'b': 5, 'd': 4}
    # Dictionary methods
    print("Keys in dictionary:", my_dict.keys())  # Output: dict_keys(['a', 'b', 'd'])
    print("Values in dictionary:", my_dict.values())  # Output: dict_values([1, 5, 4])
    print("Items in dictionary:", my_dict.items())  # Output: dict_items([('a', 1), ('b', 5), ('d', 4)])
    print("Length of dictionary:", len(my_dict))  # Output: 3
    print("Is 'a' a key in dictionary?", 'a' in my_dict)  # Output: True

#statistics
#central tendency - measures the center of a dataset, using mean, median, and mode, 
# tells where the most of the data lies on the dataset
#example
data = {
    'values': [10, 20, 20, 30, 40]
}
df = pd.DataFrame(data)
mean_value = df['values'].mean()
median_value = df['values'].median()
mode_value = df['values'].mode()[0]
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)

#dispersion - measures the spread of a dataset, using range, variance, and standard deviation
# tells how much the data varies with respect to the central tendency           
#example
#percentile - indicates the value below which a given percentage of observations fall
percentile_25 = df['values'].quantile(0.25)
percentile_75 = df['values'].quantile(0.75)
#range - measure of data spread
range_value = df['values'].max() - df['values'].min()

#variance - measue of spread of data from the mean, squared difference
variance_value = df['values'].var()
#std - - measue of spread of data from the mean, square root. 
# std is beter then variance because it gives the result accuratly based on the values in dataset
std_dev_value = df['values'].std()
print("Range:", range_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)

#IQR - Interquartile range is the difference between the 25th and 75th percentiles.
#It describes the middle 50% of the observations, and if they are spaced widely apart, their interquartile range will be large.
#It is useful even if the extreme values are not accurate, as it is insensitive to them.
#It is not amenable to mathematical manipulation.

iqr_value = percentile_75 - percentile_25
print("Interquartile Range (IQR):", iqr_value)

#measure of shape - skewness and kurtosis
#skewness - measure of asymmetry of the distribution, close to 0 indicates a symmetric distribution
#positive skewness indicates a distribution with an asymmetric tail extending toward more positive values
#negative skewness indicates a distribution with an asymmetric tail extending toward more negative values
#kurtosis - measure of the "tailedness" of the distribution
#data with heavy tails will have high kurtosis, while data with light tails will have low kurtosis.
#It provides insights into the presence of outliers and the overall shape of the distribution.
skewness_value = df['values'].skew()
kurtosis_value = df['values'].kurtosis()
print("Skewness:", skewness_value)
print("Kurtosis:", kurtosis_value)

#covariance and correlation
#covariance - measure of how two variables change together
#positive covariance indicates that as one variable increases, the other tends to increase
#negative covariance indicates that as one variable increases, the other tends to decrease
#correlation - standardized measure of the relationship between two variables, ranging from -1 to 1
#positive correlation indicates a strong direct relationship, while negative correlation indicates a strong inverse relationship
covariance_value = df['values'].cov(df['values'])
correlation_value = df['values'].corr(df['values'])
print("Covariance:", covariance_value)
print("Correlation:", correlation_value)

#probability - likelihood of an event occurring. chance of event occurance lies
#between 0 and 1, 0 means impossibility of occurance, 1 means certainity of occurance
#example
probability_event = 0.8  # 80% chance of an event occurring
print("Probability of event:", probability_event)

#random variable - randomaly occurance of the ouptut 
#descrete random variable - where the number of value is limited
#rolling a dice - only 6 ouputs are expected, 1-6, these varable can take only selected values in certain range
#continuous random variable - where the number of value is infinite, these varable can take any values in certain range
#example - measuring the height of students in a class, any hieght is possible

#probability distrubution - statistical function that defines the 
# range of possible values and thier associated probability of random variable

#discrete probability disribution - 
#A discrete probability distribution is a statistical function that describes the probabilities of outcomes for a discrete random variable.
#A discrete random variable can take only specific, separate values (like 1, 2, 3, ...).
#The distribution assigns a probability to each possible value.
#The sum of all probabilities is always 1.

#types of #discrete probability disribution -
#bernoulli distribution - A Bernoulli distribution models a single trial with two outcomes: "success" (1) with probability p, and "failure" (0) with probability 1−p.
#example 
from scipy.stats import bernoulli
p = 0.6
rvs = bernoulli.rvs(p, size=10)      # random samples of 0/1
pmf0 = bernoulli.pmf(0, p)           # P(X=0) = 1-p
pmf1 = bernoulli.pmf(1, p)           # P(X=1) = p
print(rvs, pmf0, pmf1)

# More Probability Distributions in Python
# ---------------------------------------
# 1. Binomial Distribution
# Models the number of successes in n independent Bernoulli trials
from scipy.stats import binom
n = 10  # number of trials
p = 0.5 # probability of success
binom_rvs = binom.rvs(n, p, size=10)
binom_pmf_5 = binom.pmf(5, n, p)  # Probability of 5 successes in 10 trials
print('Binomial samples:', binom_rvs)
print('P(X=5) in Binomial:', binom_pmf_5)

# 2. Poisson Distribution
# Models the number of events in a fixed interval of time/space
from scipy.stats import poisson
mu = 3  # average rate (lambda)
poisson_rvs = poisson.rvs(mu, size=10)
poisson_pmf_2 = poisson.pmf(2, mu)  # Probability of 2 events
print('Poisson samples:', poisson_rvs)
print('P(X=2) in Poisson:', poisson_pmf_2)

# 3. Uniform Distribution
# All outcomes in an interval are equally likely
from scipy.stats import uniform
uniform_rvs = uniform.rvs(loc=0, scale=1, size=10)
uniform_pdf_05 = uniform.pdf(0.5, loc=0, scale=1)
print('Uniform samples:', uniform_rvs)
print('PDF at 0.5 in Uniform:', uniform_pdf_05)

# 4. Normal (Gaussian) Distribution
# Bell-shaped curve, most common continuous distribution
from scipy.stats import norm
mu = 0    # mean
sigma = 1 # standard deviation
normal_rvs = norm.rvs(mu, sigma, size=10)
normal_pdf_0 = norm.pdf(0, mu, sigma)
print('Normal samples:', normal_rvs)
print('PDF at 0 in Normal:', normal_pdf_0)

# 5. Exponential Distribution
# Models time between events in a Poisson process
from scipy.stats import expon
expon_rvs = expon.rvs(scale=1, size=10)
expon_pdf_1 = expon.pdf(1, scale=1)
print('Exponential samples:', expon_rvs)
print('PDF at 1 in Exponential:', expon_pdf_1)

# Explanation:
# - Binomial: Discrete, counts successes in fixed trials (e.g., coin tosses)
# - Poisson: Discrete, counts events in fixed interval (e.g., arrivals per hour)
# - Uniform: Continuous, all values in interval equally likely
# - Normal: Continuous, bell curve, many natural phenomena
# - Exponential: Continuous, time until next event (e.g., time between arrivals)
# Each distribution has .rvs (random samples), .pmf (probability mass function for discrete), .pdf (probability density function for continuous)

# =============================
# Pandas and NumPy Concepts for Data Analysis
# =============================
# NumPy Concepts:
# - Creating arrays: np.array, np.zeros, np.ones, np.arange, np.linspace, np.eye
# - Array operations: addition, subtraction, multiplication, division, power
# - Statistical operations: mean, sum, min, max, std
# - Reshaping: .reshape()
# - Indexing and slicing
# - Random number generation: np.random.seed, np.random.normal, np.random.uniform
# - Central limit theorem, standard error
# - Hypothesis testing: t-test, p-value, null/alternative hypothesis
# - Covariance, correlation
# - Outlier detection, trimmed mean
# - Data generation for analysis

# Pandas Concepts:
# - Creating DataFrames from dict, list, or file (pd.DataFrame, pd.read_csv, pd.read_excel)
# - Data selection: .head(), .info(), .describe(), .select_dtypes()
# - Data manipulation: .concat(), .groupby(), .sum(), .mean(), .median(), .mode(), .std(), .var(), .quantile(), .max(), .min(), .count(), .value_counts()
# - Handling missing data: .dropna(), .fillna(), replacing with mean/median/mode
# - Outlier treatment: boxplot, trimming
# - Feature engineering: creating new columns, encoding categorical variables
# - Data preprocessing: scaling (StandardScaler), encoding (OneHotEncoder), pipelines
# - Data visualization: matplotlib, seaborn (boxplot, distplot)
# - Data splitting: train_test_split
# - Regression and classification: LinearRegression, LogisticRegression
# - Model evaluation: mean_squared_error, accuracy_score, classification_report
# - Advanced analysis: bivariate analysis, central tendency, dispersion, range, coefficient of variation
# - Inferential statistics: population/sample, estimation, confidence interval, hypothesis testing

# Example: Creating a DataFrame
import pandas as pd
import numpy as np

dicti = {'name': ['Deepak', 'Swati'], 'Lastname': ['Pandey', 'Dubey'], 'Place': ['Saibasa', 'Semari'], 'Age': [22, 38]}
df = pd.DataFrame(dicti)
print(df)

# Example: Reading data from Excel
# df2 = pd.read_excel("Super_store.xlsx")
# print(df2.head())

# Example: Data selection and summary
# print(df2['Unit Price'].sum())
# print(df2.describe())

# Example: Concatenating DataFrames
# comb = pd.concat([df, df2], axis=1)
# print(comb)

# Example: Handling missing values
# df2.dropna()
# df2.fillna(df2.mean())

# Example: Outlier detection
# import seaborn as sns
# sns.boxplot(df2['Unit Price'])
# plt.show()

# Example: Feature engineering
# df2['New_Column'] = df2['Unit Price'] * 2

# Example: Data preprocessing pipeline
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# numeric_features = ['Unit Price', 'Age']
# numeric_transformer = StandardScaler()
# categorical_features = ['Place']
# categorical_transformer = OneHotEncoder()
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', numeric_transformer, numeric_features),
#         ('cat', categorical_transformer, categorical_features)
#     ])
# pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
# df_processed = pipeline.fit_transform(df)

# Example: Central tendency and dispersion
# mean = df2['Unit Price'].mean()
# median = df2['Unit Price'].median()
# mode = df2['Unit Price'].mode()[0]
# std = df2['Unit Price'].std()
# var = df2['Unit Price'].var()
# range_val = df2['Unit Price'].max() - df2['Unit Price'].min()

# Example: Covariance and correlation
# cov = df2['Unit Price'].cov(df2['Age'])
# corr = df2['Unit Price'].corr(df2['Age'])

# Example: Inferential statistics
# import scipy.stats as stats
# z, pvalue = stats.ttest_ind(df2['Unit Price'], df2['Age'])
# print(z, pvalue)

# Example: Data visualization
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(df2['Unit Price'])
# plt.show()

# For more advanced examples, see the scripts in Practice/Data analysis folder.

############################################################
# Detailed Pandas and NumPy Concepts for Data Analysis
############################################################

# =============================
# NumPy Concepts
# =============================
# 1. Creating Arrays
import numpy as np
arr1 = np.array([1, 2, 3])  # From list
arr2 = np.zeros(5)           # Array of zeros
arr3 = np.ones(5)            # Array of ones
arr4 = np.arange(0, 10, 2)   # Array from 0 to 8, step 2
arr5 = np.linspace(0, 1, 5)  # 5 evenly spaced numbers from 0 to 1
arr6 = np.eye(3)             # 3x3 identity matrix
print(arr1, arr2, arr3, arr4, arr5, arr6)

x = np.array(['Hello','World'])
y = np.array(['Welcome', 'Learners'])
result = np.char.add(x,y)
print(result)

# 2. Array Operations
arrA = np.array([1, 2, 3])
arrB = np.array([4, 5, 6])
print('Addition:', arrA + arrB)
print('Multiplication:', arrA * arrB)
print('Mean:', np.mean(arrA))
print('Std:', np.std(arrA))

# 3. Reshaping
arr7 = np.arange(12)
print('Reshaped:', arr7.reshape(3, 4))

# 4. Indexing and Slicing
print('First element:', arr7[0])
print('First 5 elements:', arr7[:5])

# 5. Random Number Generation
np.random.seed(42)
rand_norm = np.random.normal(0, 1, 5)
rand_uniform = np.random.uniform(0, 1, 5)
print('Normal:', rand_norm)
print('Uniform:', rand_uniform)

# 6. Central Limit Theorem & Standard Error
# CLT: Sample means approach normal distribution as sample size increases
# Standard error: std / sqrt(n)

# 7. Hypothesis Testing
from scipy import stats
group1 = np.random.normal(10, 2, 100)
group2 = np.random.normal(12, 2, 100)
z, p = stats.ttest_ind(group1, group2)
print('t-test:', z, p)

# 8. Covariance & Correlation
print('Covariance:', np.cov(group1, group2))
print('Correlation:', np.corrcoef(group1, group2))

# 9. Outlier Detection
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(group1)
plt.show()

# 10. Trimmed Mean
print('Trimmed mean:', stats.trim_mean(group1, 0.1))

# =============================
# Pandas Concepts
# =============================
import pandas as pd
# 1. Creating DataFrames
# From dict
df = pd.DataFrame({'A': [1,2], 'B': [3,4]})
print(df)
# From file
# df2 = pd.read_csv('file.csv')
# df3 = pd.read_excel('file.xlsx')

# 2. Data Selection
# .head(), .info(), .describe()
print(df.head())
print(df.info())
print(df.describe())

# 3. Data Manipulation
# .concat(), .groupby(), .sum(), .mean(), .median(), .mode(), .std(), .var(), .quantile(), .max(), .min(), .count(), .value_counts()
df2 = pd.DataFrame({'A': [5,6], 'B': [7,8]})
comb = pd.concat([df, df2], axis=0)
print(comb)

# 4. Handling Missing Data
# .dropna(), .fillna(value)
df_missing = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
print(df_missing.dropna())
print(df_missing.fillna(0))

# 5. Outlier Treatment
sns.boxplot(df['A'])
plt.show()

# 6. Feature Engineering
# Creating new columns, encoding categorical variables
df['C'] = df['A'] * 2
print(df)
df_cat = pd.DataFrame({'cat': ['a', 'b', 'a']})
print(pd.get_dummies(df_cat))

# 7. Data Preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
numeric_features = ['A']
numeric_transformer = StandardScaler()
categorical_features = ['cat']
categorical_transformer = OneHotEncoder()
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
# df_processed = pipeline.fit_transform(df)

# 8. Central Tendency and Dispersion
print('Mean:', df['A'].mean())
print('Median:', df['A'].median())
print('Mode:', df['A'].mode()[0])
print('Std:', df['A'].std())
print('Var:', df['A'].var())
print('Range:', df['A'].max() - df['A'].min())

# 9. Covariance and Correlation
df_cov = pd.DataFrame({'X': [1,2,3], 'Y': [4,5,6]})
print('Covariance:', df_cov['X'].cov(df_cov['Y']))
print('Correlation:', df_cov['X'].corr(df_cov['Y']))

# 10. Inferential Statistics
# Population/sample, estimation, confidence interval, hypothesis testing
z, pvalue = stats.ttest_ind(group1, group2)
print('t-test:', z, pvalue)

# 11. Data Visualization
plt.plot(df['A'])
plt.title('Line Plot of A')
plt.show()
sns.distplot(df['A'])
plt.show()

# 12. Data Splitting
from sklearn.model_selection import train_test_split
X = df[['A']]
y = df['B']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 13. Regression & Classification
from sklearn.linear_model import LinearRegression, LogisticRegression
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)

# 14. Model Evaluation
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report
print('MSE:', mean_squared_error(y_test, pred))
# For classification: accuracy_score, classification_report

# 15. Advanced Analysis
# Bivariate: .cov(), .corr()
# Central tendency: .mean(), .median(), .mode()
# Dispersion: .std(), .var(), .max() - .min()
# Coefficient of variation: .std() / .mean()

############################################################
# End of Detailed Pandas and NumPy Concepts
############################################################


#db connection
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='your_db'
)
cursor = conn.cursor()
cursor.execute('SHOW TABLES;')
for table in cursor:
    print(table)
conn.close()

"""
Difference between Multiprocessing and Multithreading in Python
=============================================================

Multiprocessing:
- Involves running multiple processes, each with its own Python interpreter and memory space.
- Useful for CPU-bound tasks (e.g., heavy computations) because each process runs independently and can utilize multiple CPU cores.
- Avoids Python's Global Interpreter Lock (GIL).

Multithreading:
- Involves running multiple threads within the same process, sharing the same memory space.
- Useful for I/O-bound tasks (e.g., file/network operations) where threads can run while others are waiting for I/O.
- In Python, threads are limited by the GIL, so only one thread executes Python bytecode at a time (not true parallelism for CPU-bound tasks).

Example: Multiprocessing
------------------------
import multiprocessing
import time

def worker(num):
    print(f"Worker {num} starting")
    time.sleep(2)
    print(f"Worker {num} done")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print("All processes finished.")

# Output: Workers run in parallel, total time ~2 seconds.

Example: Multithreading
-----------------------
import threading
import time

def thread_worker(num):
    print(f"Thread {num} starting")
    time.sleep(2)
    print(f"Thread {num} done")

threads = []
for i in range(3):
    t = threading.Thread(target=thread_worker, args=(i,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print("All threads finished.")

# Output: Threads run concurrently, total time ~2 seconds (for I/O-bound tasks).

Summary:
--------
- Use multiprocessing for CPU-bound tasks to achieve true parallelism.
- Use multithreading for I/O-bound tasks to improve responsiveness.
- Both can be used together for complex applications.
"""


