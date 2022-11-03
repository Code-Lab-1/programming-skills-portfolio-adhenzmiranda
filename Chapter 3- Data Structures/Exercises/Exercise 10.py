#Write a program that takes a string as input and outputs the #last character of that string.

text = input()
rev = text[::-1]
last = rev[0:1]
print(last)