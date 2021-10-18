#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""

def convertTemp(temp, temptype):
    if temptype == 'C':
        newtemp = (temp * 1.8) + 32
        return newtemp
    
    if temptype == 'F':
        newtemp = (temp - 32) * .5556
        return newtemp
    
if __name__ == "__main__":
    print(convertTemp(10,'C'))
    print(convertTemp(32,'F'))