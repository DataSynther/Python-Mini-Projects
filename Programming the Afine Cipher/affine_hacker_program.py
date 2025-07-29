# Affine Cipher Hacker 

import pyperclip, affine_cipher_encryption, cryptomath, detectEnglish

SILENT_MODE = False

def main():
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    hackerMessage = hackAffine(myMessage)

    if hackerMessage != None:
        # The plaintext is displayed on the screen. For the converience of
        # the user, we copy the text of the code to the clipboard:
        print('Copying hacked message to clipboard.')
        print(hackerMessage)
        pyperclip.copy(hackerMessage)
    else: 
        print('Failed to hack encryption.')

def hackAffine(message):
    print('Hacking ........')

    # Using Brute-force by looping through every possible key
    for key in range(len(affine_cipher_encryption.symbols)**2): # Cause earlier we saw that the number of keys can be at max number of len of symbols set square
        keyA = affine_cipher_encryption.getKeyParts(key)[0]
        if cryptomath.gcd(keyA,len(affine_cipher_encryption.symbols)) != 1:
            print('Found a Key Value')
            continue

        decryptedText = affine_cipher_encryption.decryptMessage(key,message)
        if not SILENT_MODE:
            print(f"Tried key {key} :  {decryptedText[:20]}")
        if detectEnglish.isEnglish(decryptedText): 
            #check with the user if the decrypted key has been found :
            print (f"\n Possible encryption hack: \n Key : {key} \n Decrypted Message : \n {decryptedText} \n Enter D for done, or just press Enter to continue hacking.")
            response = input('>')

        if response.strip().upper().startswith('D'):
            return decryptedText 
        
    return None

# If affine hacker script runs instead of imported as module call the main function
if __name__ == '__main__':
    main()
