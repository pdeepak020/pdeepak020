# Import the library

import matplotlib.pyplot as plt
%matplotlib inline

# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

# create object
RedCircle = Circle(10,'red')

#to find out the methods which can be used 

# dir(RedCircle)
#to print radius
RedCircle.radius
#to set new value of radius
RedCircle.radius=11
RedCircle.radius #value will be 11

#call method
RedCircle.drawCircle()

#to create blue circle with given radius
BlueCircle=Circle(radius=2,color='blue')
BlueCircle.drawCircle()