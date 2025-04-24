
# to eliminate given elemnet from list
class Solution(object):
    def removeElement(self, nums, val):
        for i in range(nums.count(val)): #nums.count(val) will help to itterate only rquired numbers of time the value occurs
            print(i)
            nums.remove(val)
        return nums
    
c=Solution()
print(c.removeElement([3,2,2,3,3], 3))  # Output:


a='100.00'
z=float(a)
print(z)

s=1**3**3
print(s)

d=2,3
print(type(d))


a=90

if (a>=90):
    print("topper")
elif ( a >70 and a<90):
    print("average")

elif ( a >50 and a<70):
    print("below average")
else:
    print("fail")

a=3
if(a>= 5):
    print(hi)
elif(2<=a<=5):
    print(%d "hello")

for i in range(1,11,2):
    print(i)


a=0
for i in range(1,11):
   a=a+i
   print(a) 


#arbitary parameter
def add(*arg):
    total = 0
    for i in arg:
        total += i
    return total

#we can not pass list or tuple as argument because we have to pass seperate values
#we can pass list or tuple as argument if we use **arg

print(add(1,4,5,6,7))  # Output: 15


#lambda function
add=lambda a,b:a+b
print(add(5,6))  # Output: 11

sub=lambda(2,3:5-4)
print(sub(5,6))  # Output: 1

add =lambda a,b,c: if ((a<1) or (b<1) or (c<1)): print("all values are positive")
print(add(2,3,4))


#map function

def squ(num):
    return num**2

lis=[32,54,4,6,7,7]
print(list(map(squ,lis)))  # Output: