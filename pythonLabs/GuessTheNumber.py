import random


def main():

    def checkGuess(userGuess,computerGuess):
        if userGuess == computerGuess:
            print(f'you guessed{userGuess} and it was right')
            return True
        elif userGuess > computerGuess:
            print('Too High')
        elif userGuess < computerGuess:
            print('Too Low')

    gameInSession = True
    computerGuess = random.randint(1,50)
    lastGuess = 0

    while gameInSession:
        userGuess = int(input('Guess a number: '))

        if checkGuess(userGuess,computerGuess):
            gameInSession = False

        lastGuessCalculation = computerGuess - lastGuess
        nextGuessCalculation = computerGuess - userGuess
        if abs(nextGuessCalculation) > abs(lastGuessCalculation):
            print('your last guess closer to the target ')
        elif lastGuess == 0:
            print('Guess again and ill tell you if its closer')
        else:
            print('your getting closer to the target')

        lastGuess = userGuess

if __name__ == '__main__':
    main()
