# Caesar-cipher
### Applied programming Sep.15
### Evdokimov Maxim Ft-290007

The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. Function cipher takes one argument: 1 - to encrypt string, -1 - to decrypt. User inputs string (ONLY lowercase english alphabet + space) with shift and then function prints the cipher.

WARNING:

	1) This program encrypt only lowercase enlish alphabet and space. Other letters and symbols won't be encrypted! 
	2) Shift must be a positive number. Otherwise program will change it to an absolute value

The Ceaser Cipher is written on Python 3. Start main.py. 

```python
	cipher(1)  # ‘i am caesar’, 3 -> ‘lcdpcfdhvdu’
	cipher(-1) # ‘lcdpcfdhvdu’, 3 -> ‘i am caesar’
```

Screenshot:

![Screenshot](https://img.imageupload.net/2020/09/15/SNIMOK-EKRANA-2020-09-15-V-17.47.16.png)


