#exercise 1
friend = {
    "first_name" :"Raven" , "last_name": "Baylon" , "age": "18" , "city": "Sharjah"
}

print(friend["first_name"])
print(friend["last_name"])
print(friend["age"])
print(friend["city"])

#exercise 2
programming_words = {
    "Booleans" : "Booleans \n -are values that denotes something that is either True and False", 
    "Input" : "Input \n -is a function that prompts the user for input",
    "Variables" : "Variables \n -lets you store a value by assigning it to a name",
    "Backslash" : "Backslash \n -is a special character, called an escape character",
    "Newlines" : "Newlines \n -is a special character that creates a new line"
}

print(programming_words["Booleans"])
print(programming_words["Input"])
print(programming_words["Variables"])
print(programming_words["Backslash"])
print(programming_words["Newlines"])


#exercise 3
programming_words = {
    "Booleans" : "Booleans \n -are values that denotes something that is either True and False", 
    "Input" : "Input \n -is a function that prompts the user for input",
    "Variables" : "Variables \n -lets you store a value by assigning it to a name",
    "Backslash" : "Backslash \n -is a special character, called an escape character",
    "Newlines" : "Newlines \n -is a special character that creates a new line",
    "Tabs" : " \n -similar to a newline, but creates a tab",
    "In-Place Operators" : " \n -are operators that are use for any numerical operations",
    "Lists" : " \n -are use to store items, and are represented using square brackets with commas separating them",
    "Floats" : " \n -is any number/integer with a decimal point",
    "Strings" : " \n -are text that are enclosed in single quotes or double quotes",
}

for word, meaning in programming_words.items():
  print(f"\n {meaning}")

#exercise 4
rivers = {
    'Singapore River': 'Singapore',
    'Amstel River': 'Amsterdam',
    'Fuji River': 'japan',
    'Pasig River': 'Philippines',
    'Shenandoah River': 'United States',
    
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThese are the rivers that are in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThese are the countries that are in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")

#exercise 5
pets = []

pet = {
    'Animal Type': 'Golden Retriever',
    'Owner': 'Marla',
}
pets.append(pet)

pet = {
    'Animal Type': 'Pomeranian',
    'Owner': 'Marie',
}
pets.append(pet)

pet = {
    'Animal Type': 'Persian Cat',
    'Owner': 'Goldie',
}
pets.append(pet)

for pet in pets:
    print(f"\nThis is the Information about the {pet['Animal Type'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")