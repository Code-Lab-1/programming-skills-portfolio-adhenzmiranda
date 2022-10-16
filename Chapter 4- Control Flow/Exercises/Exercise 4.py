#exercise 4
age = int(input())

if age < 2:
  print('person is a baby')
elif age == 2 or age <4:
  print('person is a toddler')
elif age == 4 or age <13:
  print('person is a kid')
elif age ==13 or age <20:
  print('person is a teenager')
elif age ==20 or age <65:
  print('person is an adult')
elif age >=65:
  print('person is an elder')