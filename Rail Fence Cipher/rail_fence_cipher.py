"""
Given a plain-text message and a numeric key, cipher/de-cipher the given text using Rail Fence algorithm. 
The rail fence cipher (also called a zigzag cipher) is a form of transposition cipher. It derives its name from the way in which it is encoded. 
Rail Fence Transposition cipher technique is the simplest transposition cipher techniqueits. 

"""

# Function to encrypt the message

def encrpt_rail_fence(text, key):

    # Create a matrix to cipher, plain text key = rows
    # length (text) = columns , filling the rail matrix
    # to dostinguish filled spaced from blank ones

    rail = [['\n' for i in range(len(text))] for j in range(key)]
    # to find the direction
    dir_down = False 
    row, col = 0,0

    for i in range(len(text)):

        # check the direction of flow
        # reverse the direction if we have just filled the top or the bottom rail
        if (row == 0) or (row == key -1):
            dir_down = not dir_down

        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1

        #find the next row using 
        #direction flag - if going 
        # down then row index + 1 
        # if going up then row index -1

        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Construct the final result 
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("".join(result))

def main():
        
    print (" \n WELCOME TO THE RAIL FENCE CIPHER \n")
    #Let the user provide the message that needs to be encrypted 
    print (" Please enter the message, that needs to ne emcrypted :")

    # Keep asking for inputs until we get the valid values 

    while True:    
        msg = input ('> ')
        if len(msg)> 0:
            break
        else :
            print (" Please enter the message ")
            continue


    # Keep asking for key until a vaild key is chosen
    while True:
        # Ask for the key for the cipher 
        print ("please enter the key value (must be > 1) or choose if you wanna go by (d)efault")
        key_input = input ('> ')

        # check for the key value 
        if key_input.isdecimal():
            key_input = int(key_input)
            if 1< key_input< len(msg):
                print (f"Your chosen Key is {key_input}")
                break
            else:
                print ( ' Please enter a valid number or choose D to use default key ') 

        if key_input in ('d', 'D', 'default'):
            print (' You are using default key for encryption ')
            key_input = len(msg)//2 # using whole number after deviding the lenth of the msg by 2 
            print (f"\nYour key value is {key_input}")
            break

    # show the final encrypted message 

    print(" Your encrypted message is \n", encrpt_rail_fence(msg,key_input))


# Call the functions

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print (" Stopped due to the following ERROR", e)
