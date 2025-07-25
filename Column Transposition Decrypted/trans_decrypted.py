"""
The steps for decrypting are as follows:

1. Calculate the number of columns you need by dividing the length of the message by the key and then rounding up.

2. Draw boxes in columns and rows. Use the number of columns you calculated in step 1. The number of rows is the same as the key.

3. Calculate the number of boxes to shade in by taking the total number of boxes (the number of rows multiplied by the number of columns) and subtracting the length of the ciphertext message.

4. Shade in the number of boxes you calculated in step 3 at the bottom of the rightmost column.

6. Fill in the characters of the ciphertext starting at the top row and going from left to right. Skip any of the shaded boxes.

7. Get the plaintext by reading the leftmost column from top to bottom, and continuing to do the same in each column.

Note that if you used a different key, you’d draw the wrong number of rows. Even if you followed the other steps in the decryption process correctly, the plaintext would be random garbage

"""

#Import nesscary libraries

import math, pyperclip

# define the decryption message

def decrypt_msg (key, msg):

    #the transposition decrypt function will simulate the "columns" and
    # 'rows' of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values

    #The number of columns and rows in our trasposition grid

    num_of_col= int(math.ceil(len(msg)/float(key)))
    num_of_rows = key

    #The number of "shaded boxes" in the last "column" of the grid
    num_of_shaded = (num_of_col * num_of_rows) - len(msg)
    plain_text = ['']*num_of_col

    #The column and row variables point to where in the grid the next 
    # character in the encrypted message will go

    col = 0
    row = 0

    for symbol in msg:
        plain_text[col] +=symbol
        col += 1 #Point to the next column

        # If there are no more columns OR we are at a shaded box, then go back
        # to the first column and the next row

        if (col == num_of_col) or ((col == num_of_col -1) and row > (num_of_rows-num_of_shaded)):
            col = 0
            row += 1


# Writing the main function 

def main():

    # Keep asking till a valid text only message is provided
    while True :

        print (" Please enter the message to decrypt")
        msg =  input ('> ')

        # Ask for the key for the cipher 
        print ("please enter the key :")
        key_input = input ('> ')

        if len(msg)> 0 and len(key_input)> 0:
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


