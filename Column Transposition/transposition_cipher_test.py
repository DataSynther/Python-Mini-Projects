"""
Corrections in the script is ongoing 
"""

# Transposition Cipher Test

import string
import random, sys
from trans_cipher import encrypt_message
from trans_decrypt_pt2 import decrypt_msg


# Writing the test scripts

def main():
    random.seed (1000) # Set the random 'seed' to a static value'

    for i in range (50): # we are running 50 tests on this 
        # Generate random messages to test

        # The message will have a random length
        words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'*random.randint(4,100)

        #Convert the message string to list to shuffle it 
        msg = list(words)
        random.shuffle(msg)
        msg = ''.join(msg) # converting the list back to string after shuffling it

        print('Test # {} : {}'.format(i+1, msg [: 20])) # I wanna show the message only for 20 chars even if it is big

        
        # Check all possible keys for each message
        for i in range(2,int(len(msg)//2)):
            
            # Define the keys 
            all_chars =string.ascii_uppercase #use only unique letters for keys
            key = ''.join(random.sample(all_chars, i))

            encrypted = encrypt_message(key,msg)
            decrypted = decrypt_msg (key,encrypted)

            # If the decryption doesn't match the original message, display
            # an error message and quit the programme

            if msg != decrypted:
                print (f'Mismatch with {msg} and {key} and it is decrypted as \n {decrypted}')
                sys.exit()

    print ('Transposition cipher test is passed')

# If transposition test is run and not imported then call the main function
       
if __name__ == '__main__':
    main()
