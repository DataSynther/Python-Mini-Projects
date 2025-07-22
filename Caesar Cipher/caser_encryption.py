""" 
The Caesar Cipher is a  shift cipher that uses addition and substraction 
to encrypt and decrypt letters. 
More info at: https://en.wikipedia.org/wiki/Caesar_cipher 

"""

# Importing Pyperclip, this helps to copy text to the clipboard
try:
    import pyperclip
except ImportError:
    pass 

# Defining everypossible symbol that can be encrypted/decrypted
# (!) One can add numbers and punctuations and encrypt those as well 
# This version of code only takes care of characters for now

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print ("""
       
                        WELCOME TO THE CEASAR CIPHER
       The Caesar Cipher encrypts letters by shifting them over a key number. For
       example, a key of 2 means the letter A will be encrypted into C, the letter 
       B into D and so on.

       Note: This particular function does encryption and decryption based on the 
       key provided by the user, this system doesnot have the intelligence to hack 
       encrypted message without the key.

       """) 

# Let the user endter if they are trying to encrypt some data or decrypt it

# Keep asking until the user provides the valid input 
while True:
    print ('Do you want to (e)ncrypt or (d)ecrypt?')
    responce = input ('> ').lower()
    if responce.startswith('e'):
        mode = 'encrypt'
        break
    elif responce.startswith('d'):
        mode = 'decrypt'
        break
    print ('Please enter the letter e or d based on your need :')


# Let the user enter the key to use for encryption / decryption
#keep askign until the user provides with a valid key 
while True:
    max_key = len(symbols) - 1
    print ('Please enter the key (0 to {}) to use',format(max_key))
    key = input ('> ').upper()
    if not key.isdecimal():
        continue

    if 0<= int(key) <=max_key:
        key = int(key)
        break





