#exercise 5
sandwich_orders = [
    'Pastrami','Breakfast Sausage Egg', 'Braised Beef', 'Pastrami',
    'Chicken', 'Roasted Grilled Cheese', 'Pastrami',
    'Turkey', 'Roasted Beef',]
finished_sandwiches = []

print("I apologize that we are indeed all out of Pastrami for today. Sorry for the inconvinience!")
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





