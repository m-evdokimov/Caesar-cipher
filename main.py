def encrypt(text, s):
    result = ''
    abc = ' abcdefghijklmnopqrstuvwxyz'
    for i in text:
        result += abc[(abc.find(i) + s) % 27]
    return result

def decrypt(text, s):
    return encrypt(text, -s)

def main():
    print(encrypt('i am caesar', 3))
    print(decrypt('lcdpcfdhvdu', 3))

if __name__ == '__main__':
    main()
