#exercise 1
print("""Twinkle, twinkle, little star,
How I wonder what you are! Up above the world so high,
Like a diamond in the sky. 
Twinkle, twinkle, little star, How I wonder what you are""")

#exercise 2
import sys
print (sys.version)

#exercise 3
from datetime import datetime
now = datetime.now()
print (now)
dt_string = now.strftime("%d/%m/%y %H:%M:%S")
print(dt_string)

#exercise 4
name = "Adhenz Miranda"
Course = "Creative Computing Year 1"
Age = "17"
print ("Name:", name, "Course:", Course, "Age:", Age)

#exercise 5
from math import pi
radius = float(input ("Input the radius of the circle to find the area : "))
print ("The initial area of the circle with the radius of " + str(radius) + " is: " + str(pi * radius**2))