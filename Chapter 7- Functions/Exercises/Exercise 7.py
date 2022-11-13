#exercise 7
#Suggest Footwear
#Write a program that will give suggested footwear based on the weather.
#Ask the user for the weather outside with three options (sunny, rainy, or snowy) and give the correct footwear suggestion (sneaker, gumboot, or boots). Each option should be written as its own function that prints a message based on the input. Expected output:

def sunny():
    print("It is sunny day, good to wear sneaker!")
 
def rainy():
    print("Oops! its raining, better wear gumbot")
 
def snowy():
    print("Wow! its snowing, better wear boot")
 
weather_today = input("Whats the weather today:")
if weather_today == "sunny":
    sunny()
elif weather_today == "rainy":
    rainy()
elif weather_today == "snowy":
    snowy()
else:
    print(f"No footwear avaibale for {weather_today}")