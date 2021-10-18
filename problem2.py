#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is scalene
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 1  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
def triangle(a,b,c):
    if a > b and a > c:
        sidea = b
        sideb = c
        hyp = a
    if b > a and b > c:
        sidea = a
        sideb = c
        hyp = b
    if c > a and c > b:
        sidea = a
        sideb = b
        hyp = c
    
    if sidea + sideb < hyp:
        result = 0
        return (result)
    
    if sidea**2 + sideb**2 > hyp**2:
        result = 1
        return (result)

    if sidea ** 2 + sideb ** 2 == hyp**2:
        result = 2
        return (result)
    
    if sidea ** 2 + sideb ** 2 < hyp**2:
        result = 3
        return (result)
    
if __name__ == "__main__":
    print(triangle(12,5,13))
    print(triangle(3,3,4))
    print(triangle(-2,1,5))
    print(triangle(1,1,5))