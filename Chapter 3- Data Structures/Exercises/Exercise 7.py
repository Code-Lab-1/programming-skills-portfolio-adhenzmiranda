#exercise 1
friends = ["Raven", "Jose", "Nathan", "Patrick"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#exercise 2
print("This is my friend {}".format(friends[0]))
print("This is my friend {}".format(friends[1]))
print("This is my friend {}".format(friends[2]))
print("This is my friend {}".format(friends[3]))

#exercise 3
favorite_transportation = ['bicycle', "airplanes", 'F1','McLaren Senna']

print("I go to work using {}".format(favorite_transportation[0]))
print("I travel overseas using {}".format(favorite_transportation[1]))
print("I like watching {}".format(favorite_transportation[2]))
print("My favourite supercar is the {}".format(favorite_transportation[3]))

#exercise 4
invited = ['Lewis Hamilton', 'Sebastian Vettel', 'Fernando Alonso']

name = invited[0].title()
print("You are inviited to my wedding " + name)

name = invited[1].title()
print("You are inviited to my wedding " + name)

name = invited [2].title()
print("You are inviited to my wedding " + name)

name = invited[0].title()
print("Sorry " + name + " can\'t go to my wedding today")
#exerecise 5

del(invited[0])
invited.insert(0, "Mick Schumacher")

name = invited[0].title()
print("You are inviited to my wedding " + name)

name = invited[1].title()
print("You are inviited to my wedding " + name)

name = invited [2].title()
print("You are inviited to my wedding " + name)

#exercise 6

#Bigger wedding table to invite more ppl
print("\nWe got a bigger wedding table!")
invited.insert(0, 'Queen Elizabeth II')
invited.insert(2, 'Robin Atkin Downes')
invited.append('Joey Bizinger')

name = invited[0].title()
print("You are inviited to my wedding " + name)

name = invited[1].title()
print("You are inviited to my wedding " + name)

name = invited[2].title()
print("You are inviited to my wedding " + name)

name = invited[3].title()
print("You are inviited to my wedding " + name)

name = invited[4].title()
print("You are inviited to my wedding " + name)

name = invited[5].title()
print("You are inviited to my wedding " + name)



# Not enough room for wedding table
print("\nSorry, we can only invite two people to dinner.")

name = invited.pop()
print("Sorry, " + name.title() + " there's not enought room at this wedding table.")

name = invited.pop()
print("Sorry, " + name.title() + " there's not enough room at this wedding table.")

name = invited.pop()
print("Sorry, " + name.title() + " there's not enough room at this wedding table.")

name = invited.pop()
print("Sorry, " + name.title() + " there's not enough room at this wedding table.")

# Two more people
name = invited[0].title()
print("You are inviited to my wedding " + name)

name = invited[1].title()
print("You are inviited to my wedding " + name)

# Empty out the list.
del(invited[0])
del(invited[0])

# Prove the list is empty.
print(invited)

#exercise 7

locations = ['Tokyo', 'Shibuya', 'Osaka', 'Akihabara', 'Kyoto']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)