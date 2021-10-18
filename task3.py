#!python3
import math
"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""


def hypotenuse(a, b):
    hyp = math.sqrt(a**2 + b**2)
    return(hyp)

assert hypotenuse(6,8) == 10

if __name__ == "__main__":  
    print(hypotenuse(6,8))
    print(hypotenuse(5,12))