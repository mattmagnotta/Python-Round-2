import random


def main():
    def checkGuess(userGuess,computerGuess):
        if userGuess == computerGuess:
            print(f'the computer guessed {computerGuess}and you guessed {userGuess}it was right')
            return True

    gameInSession = True
    upperBound = 1
    lowerBound = 500000
    userGuess = int(input('Guess a number between 1-50'))
    lastGuess = 0

    while gameInSession:

        computerGuess = random.randint(int(upperBound),int(lowerBound))

        if checkGuess(userGuess,computerGuess):
            gameInSession = False
            if computerGuess > userGuess:
                upperBound = computerGuess
            else:
                lowerBound = computerGuess
        print(computerGuess)



if __name__ == '__main__':
    main()
