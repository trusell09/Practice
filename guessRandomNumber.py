import random 


# #user guesses

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Whoops. You are a bit low!")
        elif guess > random_number:
            print("OOF! Guess is a bit high!")
    
    print(f"Holy Smokes! You guessed the random number: {random_number}!!!!!")

guess(20)



#computer guesses the random number 

# def comp_guess(x):
#     low = 1 
#     high = x
#     feedback = ""
#     while feedback != "c":
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low #or high
#         feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
#         if feedback == "h":
#             high = guess - 1
#         elif feedback == "l":
#             low = guess + 1
#     print(f"Sweet! The computer guessed the number,{guess}!!!!!")

# comp_guess(50)