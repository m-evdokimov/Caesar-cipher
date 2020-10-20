import logging
import time


def cipher(method=1):
    logging.info('in cipher function ({})'.format('encrypting' if method == 1 else 'decrypting'))
    text = input('input string: ')
    logging.info('input string: {}'.format(text))
    s = None
    while 1:
        try:
            s = abs(int(input('Input shift: ')))
            logging.info('input shift: {}'.format(s))
        except ValueError:                          #finding non-int values
            logging.info('got an exception, refreshing...')
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
    logging.info('returning the result: {0}'.format(result))
    print(result)

def main():
    logging.basicConfig(level='INFO',
                        filename='log.txt',
                        format='%(levelname)s %(asctime)s - %(message)s')
    logging.info('starting...')
    while 1:
        ans = input('What you want to do? (1 - encrypt, -1 - decrypt, 0 - exit): ')
        logging.info('user input from dialogue window: {0}'.format(ans))
        if ans == '1':
            cipher()
        elif ans == '-1':
            cipher(-1)
        elif ans == '0':
            break
        else:
            logging.info('got incorrect key, getting back...')
            print('Incorrect input! Try again!')

    logging.info('program was closed correcly!')


if __name__ == '__main__':
    main()
