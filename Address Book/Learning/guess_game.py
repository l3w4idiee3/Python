import random
def guess_number_game():
    randomNumber = generateRandomNumber()
    max_attempt = 5
    attempts = 0
    
    while attempts < max_attempt:
        attempts += 1
        prompt = int(input("Enter your guess: "))
        if prompt == randomNumber:
            guesseCorrectly = True
            print("Congratulation you have guessed correctly!!!")
        elif prompt < randomNumber:
            print("Your number is too low")
        else:
            print("Your number is to high")
    print("Sorry, you have run out of attempts. The correct number was", randomNumber)
def generateRandomNumber():
    return random.randint(1, 100)

guess_number_game()