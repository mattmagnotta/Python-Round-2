import random

def main():
    play_again = True

    while play_again:
        rounds = input('How many rounds do you want to play? ')
        eyes = [':',';','8']
        noses = ['<','>','-']
        mouth = ['p','0','D']

        count = 0

        while count <= int(rounds):
            count += 1
            print(f"{random.choice(eyes)}{random.choice(noses)}{random.choice(mouth)}")

        play_again = input('Thanks for using Emoticon, do you want to play again?')

        if play_again == 'n':
            play_again = False


if __name__ == '__main__':
    main()
