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







