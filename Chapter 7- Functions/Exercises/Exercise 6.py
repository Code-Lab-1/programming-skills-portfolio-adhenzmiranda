#exercise 6
#Sum of numbers
#Write a function that takes two arguments and returns their sum.

def sum_of_number(a, b):
    return a + b
 
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
ttl = sum_of_number(num1, num2)
print(f"{num1} + {num2} = {ttl}")