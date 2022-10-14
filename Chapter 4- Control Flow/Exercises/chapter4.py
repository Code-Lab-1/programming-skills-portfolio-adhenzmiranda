#exercise 1
#passing verison
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'red'

#failing version
if alien_color == 'green':
    print("You just earned 5 points!")

#exercise 2
#if-block
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#else-block
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 15 points!")

#exercise 3
#green = 5 points
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

#yellow = 10 points
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
#red =  15 points
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

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

#exxercise 5
fav_fruits = ['Watermelon', 'Apples', 'Passion Fruit']

if 'Watermelon' in fav_fruits:
    print("You really like Watermelon!")
if 'apples' in fav_fruits:
    print("You really like apples!")
if 'blueberries' in fav_fruits:
    print("You really like blueberries!")
if 'Passion Fruit' in fav_fruits:
    print("You really like Passion Fruit!")
if 'peaches' in fav_fruits:
    print("You really like peaches!")