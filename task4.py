#!python3
import math

"""
Create a function that determines the area of a circle if given the radius
1 input parameter
float: radius

return: float area for the circle

note: Area of a circle is given by A = pi*(square of the radius)
You may want to use the math module to complete this problem
"""

def area(radius):
    pi = math.pi
    a = pi*(radius**2)
    return a


assert round(area(2),2) == 12.57

if __name__ == "__main__":  
    print(round(area(1),2))
    print(round(area(2),2))