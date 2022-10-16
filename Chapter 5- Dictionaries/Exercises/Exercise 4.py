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
