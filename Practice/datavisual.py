#data visualisation - matplotlib seaborn
#statistics - linear algebra , basic statistics ( descriptive statistics , ), probability distribution - 
# probability - binomial , poission, normal destribution
#and more

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

a=[12,2,34,4]
b=[423,532,5,5,5,5,5224]

y=np.cos(a)
x=np.sin(b)
z=np.tan(a)

#plt.plot(a,y)
#plt.show()

plt.subplot(2,2,1)
plt.plot(y,a,color='r', label = 'sin' )
plt.legend()

plt.subplot(2,2,2)
plt.plot(x,b,color='g', label = 'sin' )
plt.legend()
#plt.show()



plt.subplot(2,2,4)
data=np.random.randn(1000)
#plt.hist(data, bin=10) # is used to get the data distrubution, if it is distributed normally (gaussian distribution) or abnormally

plt.subplot(2,2,3)
#plt.bar(x,b)
#c=['A',]
#plt.pie(dat,bin=100)

#plt.show()

data1=sn.load_dataset('tips')
data1.groupby(["sex","day"])["total_bill"].max().unstack()
print(data1)
plt.show()

#


