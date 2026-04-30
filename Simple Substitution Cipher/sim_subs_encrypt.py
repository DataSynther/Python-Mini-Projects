"""
Simple Substitution Cipher
A simple substitution cipher is a method of encryption where each letter in the 
plaintext is replaced by a corresponding letter from a fixed, scrambled alphabet.
It is resistant to brute-force attacks because the number of possible keys is 
extremely large, making exhaustive search practically impossible.

"""
import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

## Fun Function to have

def substitution_cipher_strength(possible_keys: int, keys_per_second: float) -> str:
    """
    Estimate time to brute-force a simple substitution cipher.
    
    Args:
        possible_keys (int): Total number of possible keys.
        keys_per_second (float): How many keys a computer can try per second.

    Returns:
        str: A statement about the feasibility of brute-force attack.
    """
    seconds = possible_keys / keys_per_second
    years = seconds / (60 * 60 * 24 * 365)

    if years > 1_000_000:
        return (f"Brute-force is impractical: {years:,.0f} years required "
                f"even at {keys_per_second:.0e} keys/sec!")
    else:
        return (f"Brute-forcing would take about {years:,.0f} years "
                f"at {keys_per_second:.0e} keys/sec.")

# Example usage:
print(substitution_cipher_strength(10**26, 10**12))

# This function makes sure that substitution is possible for all the letters/ characters in the char set
def keyIsValid(key):
    keyList = list(key)
    letterList = list(LETTERS)
    keyList.sort()
    letterList.sort()

    return keyList == letterList

def translateMessage (key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # for decrypting we can use the same code as encrypting. 
        # We just need to swap where the key and LETTERS strings are used
        charsA, charsB = charsB,charsA

    #Loop through each symbol in the message
    for symbol in message :
        if symbol.upper() in charsA:
            #Encrypt or DEcrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            #Just add the symbol without encrypting or decrypting
            translated += symbol
    return translated

def encryptMessage(key, message):
    return translateMessage(key, message,'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message,'decrypt')

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return"".join(key)

def main():
    myMessage = """If a man is offered a fact which goes against his
        instincts, he will scrutinize it closely, and unless the evidence
        is overwhelming, he will refuse to believe it. If, on the other
        hand, he is offered something which affords a reason for acting
        in accordance to his instincts, he will accept it even on the
        slightest evidence. The origin of myths is explained in this way.
        -Bertrand Russell'"""
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt' # Set to 'encrypt' or 'decrypt'.
    
    if keyIsValid(myKey)== False:
        sys.exit('There is an error in the key or symbol set.')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')   

if __name__ == '__main__':
    main()