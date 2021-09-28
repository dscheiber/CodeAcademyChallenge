#1. Convert radians into degrees
#Write a function in Python that accepts one numeric parameter. 
#This parameter will be the measure of an angle in radians. 
# The function should convert the radians into degrees and 
# then return that value.

#While you might find a Python library to do this for you, 
# you should write the function yourself. One hint you get is 
# that you'll need to use Pi in order to solve this problem. 
# You can import the value for Pi from Python's math module.

import math

pi = math.pi

def radianstodegrees_basic(rad):
    try: 
        if abs(rad) >=0 and abs(rad) <= 2*pi:
            degrees = rad * 180 / pi
        elif abs(rad) > 2*pi:
            rad = rad % (2*pi)
        degrees = rad * 180 / pi
        return degrees
    except:
        return "Not a valid input."

def radianstodegrees_userinput():
    rad = input("Enter a radian value to be converted to degrees \n")
    inputvalidated = 0
    while inputvalidated == 0:
        try:
            rad = float(rad)
            inputvalidated = 1
        except:
            rad = input("Enter a numerical value, no more jokes \n") 
    if abs(rad) >=0 and abs(rad) <= 2*pi:
        degrees = rad * 180 / pi
    elif abs(rad) > 2*pi:
        rad = rad % (2*pi)
    degrees = rad * 180 / pi
    return degrees

##demo
print("2 radians to degrees is:")
print(radianstodegrees_basic(2))
print("2pi radians to degrees is:")
print(radianstodegrees_basic((2*pi)))
print("-2 radians to degrees is:")
print(radianstodegrees_basic(-2))
print("A bogus input (chicken) to degrees is:")
print(radianstodegrees_basic('chicken'))

print(radianstodegrees_userinput())

