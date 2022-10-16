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