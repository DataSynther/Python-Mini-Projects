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
    key1 = input ('> ').upper()
    if not key1.isdecimal():
        key = int(key1)
        continue

    if 0<= int(key1) <=max_key:
        key = int(key1)
        break

# Let the user ente the message to encrypt/ decrypt
print ('Enter the message to {}', format (mode))
msg = input ('> ').upper() # since our symbol list only has uppercase characters

#stores the encrypted/decreypted form of the message
translated = '' 

# Encrypt/Decrypt each symbol in the message 

for symbol in msg :
    if symbol in symbols:
        #Get the encrypted (or decrypted) number for this symbol
        num = symbols.find(symbol)
        if mode == 'encrypt':
            num = num+key
        elif mode == 'decrypt':
            num = num-key


        #Handle the wrap around if number is larger than the length of symbols (or less than zero)
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)
        
        #Add encrypted/ decrypted number's symbol to translated:
        translated = translated + symbols [num]

    else:
        #Just add the symbol without encrypting/decrypting
        translated = translated + symbol

#Display the encrypted / decrypted string to the screen:
print (translated)

try:
    pyperclip.copy(translated)
    print (f" Full {mode}ed text copied to clipboard")
except:
    pass



