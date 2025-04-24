#numpy - numerical python
#pandas - data handaling
#matplot seaborn - visualization libraries
#scipy - scientific python
#stats model - statistical model
#scikit learn- data preprocessing, base for machine learning, for large data

#for unstructured data (data like image , text, video, signal)
#deep learing models are used- keras, tensorflow (application oriented- user friendly), pytorch (mainly oops concept)

#datascientist skills - 
#program
#mathematics and statistcs
#domain understanding (data


#sequence datatype- 
#list - [], multiple data, heterogeneous data, mutable(changeable), ordered(indexing), duplicates are allowed, index start 0, 1D data.
#set- {}, multiple data, heterogeneous data, imutable(not changeable), duplicates not allowed, index starts with 0, 1D data.
#tuple- (), multiple data, heterogeneous data, imutable(not changeable), duplicates are allowed, index start 0, 1D data.

#mutable/imutable meaning

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
a=[1,2,3]
a[0]=2
print(a)  #[2,2,3] mutable
a.append('deepak')
print(a) #[2,2,3,'deepak'] #mutable
a.extend(['pandey',3])
print(a) #mutable
a.insert(2,'rishi')
print(a)
a.pop(3)
print(a) #[2, 2, 'rishi', 'deepak', 'pandey', 3]
a.remove('rishi')
print(a) #[2, 2, 'deepak', 'pandey', 3]
print(len(a)) #5



#img=plt.imshow
y=np.random.randint(1,20,(3,4)) #2D array with 3 rows and 4 coloumns

#numpy is used for numerical data and image processing

print(y)
x.ndim #dimention
x.shape #return the rows and coloiunms
y.reshape(4,3) # reshape the data, only combination with result of 12(number of element) should be given. like - 3,4 6,2 2,6
y.reshape(4,-1) # -1 is replaced the required value that is 3
y.reshape(-1,2) # -1 will replace with 6
y.mean()
y.sum()
y.sum(axis=0) # sum of each column
y.sum(axis=1) #sum of each row
y.max()
y.max(axis=0) #max of each column
y.max(axis=1) #max of each row
y.min()
y.min(axis=0) #min of each column
y.min(axis=1) #min of each row
y.std()
y.std(axis=0) #standard deviation of each column
y.std(axis=1) #standard deviation of each row
y.var()
y.var(axis=0) #variance of each column
y.var(axis=1) #variance of each row
y.cumsum()
y.cumsum(axis=0) #cumulative sum of each column
y.cumsum(axis=1) #cumulative sum of each row
y.cumprod()
y.cumprod(axis=0) #cumulative product of each column
y.cumprod(axis=1) #cumulative product of each row
y.argmin()
y.argmin(axis=0) #index of min of each column
y.argmin(axis=1) #index of min of each row
y.argmax()
y.argmax(axis=0) #index of max of each column
y.argmax(axis=1)
np.where(y>10,2,30) 


