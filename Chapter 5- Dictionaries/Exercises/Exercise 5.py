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