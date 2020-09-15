def cipher(method=1):
    text = input('Input string: ')
    s = int(input('Input shift: '))
    if method == -1:
        s *= -1
    result = ''
    abc = ' abcdefghijklmnopqrstuvwxyz'
    for i in text:
        result += abc[(abc.find(i) + s) % 27]
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
            raise KeyError('Incorrect input')


if __name__ == '__main__':
    main()
