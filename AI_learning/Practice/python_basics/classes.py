# Import the library

import matplotlib.pyplot as plt
#%matplotlib inline  - this is used in jupyter notebook to show the plot inline once code is executed
# Create a class Circle

class Circle:
    
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
        plt.figure()  # Create a new figure to provide the size and resolution of the figure
        ax = plt.gca() # Get the current axes - this is used to set the limits of the axes
        ax.set_xlim(-self.radius-1, self.radius+1)
        ax.set_ylim(-self.radius-1, self.radius+1)
        ax.set_aspect('equal', adjustable='box')
        ax.add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.show()  

# create object
RedCircle = Circle(10,'red')

#to find out the methods which can be used 

# Access the radius
RedCircle.radius
RedCircle.radius
# Set a new value for the radius
RedCircle.radius=11
RedCircle.radius #value will be 11
# The radius is updated to 11 after reassignment
RedCircle.radius
#call method
RedCircle.drawCircle()

#to create blue circle with given radius
blue_circle = Circle(radius=2, color='blue')
blue_circle.drawCircle()

#print(dir(__str__)) # Fixed NameError: __str__ is not defined