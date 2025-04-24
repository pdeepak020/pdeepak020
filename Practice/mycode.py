print("Heloo")
print("deepak") # print in seperate line

print("Hello", "deepak") #print in same line by using comma

print(23) # to print integer no quotes
print(23+24) #to add two numbers

# in python variable is the name given to memory location in program 

name = "deepak"

print(name)
print("my name", name)

#identifers are variable or function or anyther name like
#name = "deepak" - here name is identifer 
# identifer can start with char like below examples
#name_class , nameClass namclass1 
#identifer should not start with numbers or special char

print(type(name)) # will print datatype of varible like - <class 'str'>

name = "sk"
name1 = 'sk'
name2 = '''sk''' # we can pass value with all the quotes like "" , '', ''' '''

name = True
print (name , name1, name2) # 

# keywords in python = these words can not be used as identifiers or variables as they are reserved words
# return, True , lambda, else, as, def, del , elif, if , pass , raise, with, yield, while , except, class , continue
# not , ... and more there
 
# Python is case sensitive language like -
# Apple and apple are different, True and true are different

# comments in python
# # is used to comment single line
# """ """ is used to comment multiline

# operators in Python
# Arithmetic operators -  + - * / % **
a = 5
b = 3
print ( a ** b ) # power operator

# Relational operators - == != > < >= <= 
print ( a == b ) # this will print bolean value True or False


# Assignment operators - = += -= *= /= %= %= **=
a += b
print(a)

#logical operators - not and or
print ( not a > b) # will print Flase as the condition is true and not true is false

#type convertion
a = 4
b = 2.3
print ( a + b) # here pythom will first convert int value to float becaue float is superior to integer and
# then add the float values this automatically done 

#type casting
c = 3
d = float(3)
print (d, c) # this manual coversion of integer to float and is know as type casting

#input
value = float(input( "enter name: ")) # float is used to type cast input value
print(value)

#String
 






