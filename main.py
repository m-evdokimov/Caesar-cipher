import logging


def cipher(method=1):
    text = input('Input string: ')
    s = None
    while 1:
        try:
            s = abs(int(input('Input shift: ')))
        except ValueError:                          #finding non-int values
            print('Incorrect input! Try again')
            continue
        break

    if method == -1:
        s *= -1
    result = ''
    abc = ' abcdefghijklmnopqrstuvwxyz'             # english alphabet for encrypting
    for i in text:
        if i in abc:
            result += abc[(abc.find(i) + s) % 27]   # add encrypted letter
        else:
            result += i                             # add other characters
    print(result)

def main():
    while 1:
        ans = int(input('What you want to do? (1 - encrypt, -1 - decrypt, 0 - exit): '))
        if ans == 1:
            cipher()
        elif ans == -1:
            cipher(-1)
        elif ans == 0:
            break
        else:
            print('Incorrect input! Try again!')


if __name__ == '__main__':
    main()
