#Return


#We need to calculate the area of a given rectangle.
#Your program needs to take the width and length as input and output the area of the rectangle.

#Complete the area function, which takes the length and width as arguments, to calculate and return the area.
#Then call the function for the given inputs.

#Sample Input 1
#7
#4

#Sample Output 1
#28

def area(x, y):
   return x*y
   

w = int(input())
h = int(input())

print (area(w,h))