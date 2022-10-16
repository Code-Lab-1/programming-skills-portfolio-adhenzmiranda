#exercise 1
question = "\nWhat topping would you like on your fabulous pizza today?"
question += "\nEnter 'done' when you are done adding your toppings: "

while True:
    topping = input(question)
    if topping != 'done':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break






