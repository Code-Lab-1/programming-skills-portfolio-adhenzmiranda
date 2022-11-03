#You are making a ticketing system.
#he price of a single ticket is $100.
#For children under 3 years of age, the ticket is free.

#Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.

#Sample Input
#18
#24
#2
#5
#42

#Sample Output
#400

total = 0
x = 0
while x<5:
    age = int(input())
    if age > 3:
        total += 100
    x+=1
print(total)