import argparse

def main():
    parser = argparse.ArgumentParser(description='enrypt a message with a cypher.')

    parser.add_argument('message', metavar='N', type=str, nargs='+',help='the message you want decoded')

    parser.add_argument('rotation', metavar='R', type=int, nargs='+',help='the shift amount of the cypher')

    args = parser.parse_args()
    rotation = args.rotation[0]
    message = args.message[0]

    def encrypt(message,rotation):
        start = ord('a')
        charNumberList = []

        for char in message:
            if char.isalpha():
                charNumberList.append(ord(char))
            else:
                charNumberList.append(char)

        charNumberRotatedList = []

        for ordChar in charNumberList:
            if str(ordChar).isalnum():
                OrderedLetter = ordChar - start
                rotated = (OrderedLetter + rotation) % 26 + start
                charNumberRotatedList.append(chr(rotated))
            else:
                charNumberRotatedList.append(ordChar)
        print("your message is:" + ''.join(charNumberRotatedList))

    encrypt(message,rotation)


if __name__ == '__main__':
    main()
