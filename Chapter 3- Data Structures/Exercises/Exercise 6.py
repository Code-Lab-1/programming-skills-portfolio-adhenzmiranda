#exercise 6
invited = ['Lewis Hamilton', 'Sebastian Vettel', 'Fernando Alonso']

name = invited[0].title()
print("You are inviited to my wedding " + name)

name = invited[1].title()
print("You are inviited to my wedding " + name)

name = invited [2].title()
print("You are inviited to my wedding " + name)

name = invited[0].title()
print("Sorry " + name + " can\'t go to my wedding today")

del(invited[0])
invited.insert(0, "Mick Schumacher")

name = invited[0].title()
print("You are inviited to my wedding " + name)

name = invited[1].title()
print("You are inviited to my wedding " + name)

name = invited [2].title()
print("You are inviited to my wedding " + name)

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

# Empty the list.
del(invited[0])
del(invited[0])

# Prove the list is empty.
print(invited)