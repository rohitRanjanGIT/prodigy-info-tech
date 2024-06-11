import random

def guessGame():
    print("The rules of this guessing game are simple. A random number will be generated, you will have to guess a number. If it matches the random number, you win. Otherwise, you will be told if your guess is greater or smaller than the randomly generated number. You will have 5 chances to guess the number.")
    
    numberOfGames = int(input("How many times would you like to play the game? "))
    totalScore = 0

    def check(randomNumber, guessedNumber):
        if randomNumber == guessedNumber:
            print("Congratulations! You have guessed the number correctly. You win!")
            return True
        elif randomNumber > guessedNumber:
            if randomNumber - 5 < guessedNumber:
                print("Your guess is close but still smaller than the random number. Try again!")
            else:
                print("Your guess is smaller than the random number. Try again!")
        else:
            if randomNumber + 5 > guessedNumber:
                print("Your guess is close but still greater than the random number. Try again!")
            else:
                print("Your guess is greater than the random number. Try again!")
        return False

    for game in range(numberOfGames):
        difficulty = str(input("Choose your difficulty level.\n1 - random range 1-20.\n2 - random range 1-50\n3 - random range 1-100\nX--------------------------x\nULTRA - 1-1000\n"))

        if difficulty == '1':
            randomNumber = random.randint(1, 20)
        elif difficulty == '2':
            randomNumber = random.randint(1, 50)
        elif difficulty == '3':
            randomNumber = random.randint(1, 100)
        elif difficulty == "ULTRA":
            randomNumber = random.randint(1, 1000)
        else:
            print("Invalid difficulty level. Please restart the game and choose a valid level.")
            return

        for chance in range(5):
            guessedNumber = int(input("Enter your guess: "))
            if check(randomNumber, guessedNumber):
                if chance == 0:
                    totalScore += 100
                elif chance == 1:
                    totalScore += 75
                elif chance == 2:
                    totalScore += 50
                else:
                    totalScore += 25
                break
            else:
                print("You have", 4 - chance, "chances left.")
        
        if not check(randomNumber, guessedNumber):
            print("Sorry, you've used all your chances. The correct number was", randomNumber)

    print("You have completed all the games.")
    print("Your total score is:", totalScore)


guessGame()
