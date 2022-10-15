#exercise 1
question = "\nWhat topping would you like on your fabulous pizza today?"
question += "\nEnter 'done' when you are done adding your toppings: "

while True:
    topping = input(question)
    if topping != 'done':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break


#exercise 2
qstn = "How old are you?"
qstn += "\nPlease type 'finish' when all the people in the queue are finished."


while True:
    age = input(qstn)
    if age == 'finish':
        break
    age = int(age)

    if age < 3:
        print("  You get in for free today's movie!!")
    elif age < 13:
        print("  Your ticket will be $10. Thank You!")
    else:
        print("  Your ticket will be $15. Please Enjoy the Movie!")


#exercise 3
loop = True
while (loop):
  print("To Infinity!!! and Beyond!!!")


#exercise 4
sandwich_orders = ['Chicken', 'Roasted Grilled Cheese', 'Turkey', 'Roasted Beef', 'Breakfast Sausage Egg', 'Braised Beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am currently working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I have finished the {sandwich} sandwich.")


#exercise 5
sandwich_orders = [
    'Pastrami','Breakfast Sausage Egg', 'Braised Beef', 'Pastrami',
    'Chicken', 'Roasted Grilled Cheese', 'Pastrami',
    'Turkey', 'Roasted Beef',]
finished_sandwiches = []

print("I'm apologize that we are indeed all out of Pastrami for today. Sorry for the inconvinience!")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm currently working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I have finished the {sandwich} sandwich.")





