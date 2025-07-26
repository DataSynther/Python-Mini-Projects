
"""
The originial code script assumes that columns are always in order 1,2,3,4... (no keyword ordering).

Modicication: 

The modified script introduces column reordering by:

- Sorting the keyword to know how columns were arranged during encryption.
- Splitting ciphertext into chunks in that sorted order.
- Reconstructing plaintext row by row in original column order.

"""

#Import nesscary libraries

import math, pyperclip

# define the decryption message

def decrypt_msg (key, msg):

    """
    Decrypt Columnar Transposition Cipher.
    `code` = keyword
    `msg` = encrypted text
    """

    # Defining number of rows, columns and number of shaded cells in the matrix

    num_of_col= int(math.ceil(len(msg)/len(key)))
    num_of_rows = len(key)
    num_of_shaded = (num_of_col * num_of_rows) - len(msg)

    # Step 1 :  Get sorted order of keyword columns 
    code =  str(key)
    indexed_code = list(enumerate(code))
    sorted_order = sorted(indexed_code, key = lambda x : (x[1],x[0]))

    # Step 2 : Calculate the length of each column (and handle the shaded boxes)

    col_lengths = [num_of_col]*len(code)

    for i in range(num_of_shaded):
        shaded_col = sorted_order[-(i+1)][0]#
        col_lengths [shaded_col] -= 1 #

    # Step 3 : Split ciphertext into chunks according to sorted order

    col_texts = {}
    pointer = 0

    for orig_index, _ in sorted_order :
        length = col_lengths [orig_index]
        col_texts[orig_index] = msg[pointer: pointer+length]
        pointer += length
    
    # Step 4 : Read row by row using original column order

    plaintext = []
    for r in range(int(num_of_col)):
        for c in range(len(code)):
            if r < len(col_texts[c]):
                plaintext.append(col_texts[c][r])

    return"".join(plaintext)

# Writing the main function 

def main():

    # Keep asking till a valid text only message is provided
    while True :

        print (" Please enter the message to decrypt")
        msg =  input ('> ')

        # Ask for the key for the cipher 
        print ("please enter the key :")
        key_input = input ('> ')

        if len(msg)> 0 and len(key_input) > 0:
            break
        else :
            print (" Either message or decryption key is not valid ")
            continue
    

    cipher_text =  decrypt_msg(key_input,msg)

    #Print the encrypted string in ciphertext to the screen with pipe after it in case there are spaces at the 
    #end of the encrypted text
    print (cipher_text,'|')
    pyperclip.copy (cipher_text)

if __name__ == '__main__':
    main()