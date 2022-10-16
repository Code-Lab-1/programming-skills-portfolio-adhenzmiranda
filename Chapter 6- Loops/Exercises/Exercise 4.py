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








