"""
Columnar Transposition involves writing the plaintext out in rows, and then reading the ciphertext off in columns one by one.

The Encryption Method is as Followed:

1. Count the number of charachters in the message and get the key .
2. Draw a row of a number of bexes equals to key (i.e. if key value = 8, then number of columns = 8)
3. Start filling the boxes  from left to right entering one character per box
4. When run out of boxes, take a now row and starts filling it
5. Once the last char is reached shade the remaining boxes ( keep note we are trying to deal with space and nulls differently)
6. Read columns one by one (if given column order, then using that else start from the first column from top to bottom) and ignore
   the shaded/ empty cells.

"""
import pyperclip

#defining the encryption function

def encrypt_message (code, msg):

    '''
     here code indicates the word using which the encryption should happen

    '''

    key = len(code)
    # Each string in the ciphertext represents a column in the grid:
    cipher_text = ['']*key

    # Loop through each column in ciphertext

    for column in range(key):
        cur_index = column

        # Keep looping until currentindex goes past the message length

        while cur_index < len(msg):

            # Write the char at current index in msg and place it columnwise
            cipher_text[column]+= msg[cur_index]

            #move the currentindex over:
            cur_index += key
        
    # Read the text in correct order:

    result = []
    for tag in sorted(list(code)):
        for i in range(len(list(code))):
            if list(code)[i] == tag:
                result.append(cipher_text[i])
    
    # finally make it a normal text 
    return "".join(result)


# Writing the main function 

def main():

    # Keep asking till a valid text only message is provided
    while True :

        print (" Please enter the message to encrypt ")
        msg =  input ('> ')

        # Ask for the key for the cipher 
        print ("please enter the key :")
        key_input = input ('> ')

        if len(msg)> 0 and len(key_input)> 0:
            break
        else :
            print (" Either message or encryption key is not valid ")
            continue
    
    cipher_text =  encrypt_message(key_input,msg)

    #Print the encrypted string in ciphertext to the screen with pipe after it in case there are spaces at the 
    #end of the encrypted text
    print (cipher_text,'|')
    pyperclip.copy (cipher_text)

if __name__ == '__main__':
    main()

    