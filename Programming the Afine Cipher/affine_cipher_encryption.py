""" AFFINE CIPHER

The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is 
mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to 
a letter. The formula used means that each letter encrypts to one other letter, and back again, meaning 
the cipher is essentially a standard substitution cipher with a rule governing which letter goes to which.
The encryption function for a single letter is E(x)=(ax+b)mod m, where a and b are the keys of the cipher, 
and m is the size of the alphabet.

Note: 

1. The key and the size of the symbol set must be realtively prime ( or coprime to each other i.e. GCD 
of key and symbol is 1)

2. Keep in mind that according to Shannon’s Maxim (“The enemy knows the system!”) we must assume hackers know 
everything about the encryption algorithm, including the symbol set and the size of the symbol set. We assume 
that the only piece a hacker doesn’t know is the key that was used. The security of our cipher program should 
depend only on the secrecy of the key, not the secrecy of the symbol set or the program’s source code.

"""

import sys, pyperclip, random
from cryptomath import gcd, find_mod_inverse
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'

def main():
    myMessage = """

        "A computer would deserve to be called intelligent 
        if it could deceive a human into  believing that it 
        was human" - Alan Turing 

        """
    myKey = 2894
    myMode = 'encrypt' 

    if myMode == 'encrypt':
        translated = encryptMessage(myKey,myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey,myMessage)

    pyperclip.copy(translated)
    print(f"Key : {myKey} \n {myMode.title()}ed text : \n {translated} \n Full {myMode}ed text copied to clipboard ")

# Calculate values like - char = (KeyA * symbol) + keyB 
def getKeyParts(key):
    keyA = key // len(symbols) # Calculates Quotient
    keyB = key % len(symbols) # Calculates Remainder
    return (keyA,keyB) # returns a tuple

# check the complexity of the key
def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit("Cipher is weak if Quotient is 1. Choose a different key.")
    if keyB == 0 and mode == 'encrypt':
        sys.exit("Cipher is weak if Remainder is 0. Choose a different key ")
    if keyA<0 or keyB<0 or keyB> (len(symbols) -1):
        sys.exit(f"Quotioent must be a positive integer and the Remainder should be between 0 and length of symbols")
    if gcd(keyA, len(symbols)) != 1:
        sys.exit(f"Key A {keyA} and the symbol set size {len(symbols)} are not relatively prime. Choose a different key.")


def encryptMessage(key,message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA,keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in symbols:
            #Encrypt the symbol 
            symbol_index = symbols.find(symbol)
            ciphertext += symbols[(symbol_index*keyA +keyB)%len(symbols)]
        else:
            ciphertext += symbol # Append the symbol without encrypting 
    return ciphertext

def decryptMessage(key,message):
    keyA,keyB = getKeyParts(key)
    checkKeys(keyA,keyB, 'decrypt')
    plaintext = '' 
    modInverseofKeyA = find_mod_inverse(keyA,len(symbols))

    for symbol in message :
        if symbol in symbols:
            #Decrypt the symbol:
            symbolIndex = symbols.find(symbol)
            plaintext += symbols[(symbolIndex - keyB)* modInverseofKeyA % len(symbols)]
        else:
            plaintext += symbol # Append the symbol without decrypting
    return plaintext
    

def getRamdomKey():
    while True:
        KeyA =  random.randint(2, len(symbols))
        keyB = random.randint(2, len(symbols))

        if gcd(KeyA, len(symbols)) == 1:
            return KeyA*len(symbols)+keyB
        
# If affine cipher is run (instead of imported as module), call
# the main() function:
if __name__ == '__main__':
    main()



