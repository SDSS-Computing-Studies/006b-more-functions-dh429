#!python3
"""
Create a function that determines the largest number in a list of values and returns it.
1 input parameter:
list: the numbers to be checked for the largest value

return: float value of the largest number

Sample assertions:
assert largest([3,10,3]) == 10
"""

def largest(numlist):
    numlist.sort()
    biggest = numlist[-1]
    return(biggest)

assert largest([3,10,3]) == 10

if __name__ == "__main__":
    print(largest([10,50,100,3000.1]))