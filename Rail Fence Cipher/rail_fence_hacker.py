"""
Given a plain-text message and a numeric key, cipher/de-cipher the given text using Rail Fence algorithm. 
The rail fence cipher (also called a zigzag cipher) is a form of transposition cipher. It derives its name from the way in which it is encoded. 
Rail Fence Transposition cipher technique is the simplest transposition cipher techniqueits. 

Note: The number of column is same as the length of the text, and the key/ depth value can take numbers >1 and less than the length of the message
using these two observations, and brute force approach we will try to decrypt the rail fence cipher


WIP : TRYING TO ADD BRUTE FORCE FEATURE 

"""
# Need this to detect the english language
# import nltk
# from nltk.corpus import words
# import string

# Importing Pyperclip, this helps to copy text to the clipboard
try:
    import pyperclip
except ImportError:
    pass 

# # Ensure the word list is available
# nltk.download('words')
# english_words = set(words.words())

# check word score based on dictionary matching 

# def word_score(text):
#     # Count how many real words are in the decrypted text
#     tokens = text.lower().split()
#     cleaned_tokens = [word.strip(string.punctuation) for word in tokens]
#     return sum(1 for word in cleaned_tokens if word in english_words)

import detectEnglish


# defining the function for decrypting for the cipher and the key value
def decrypt_rail_fence(cipher,key):
    
    #Create the matrix to cipher
    #plain text key = rows and length of text = column
    #filling the rail matrix to distinguish filled spaces from blank ones

    rail = [['\n' for i in range(len(cipher))] for j in range(key)]

    #to find the letter filling direction
    dir_down = None 
    row, col = 0,0 

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key -1:
            dir_down = False
    
        #Place the marker 
        rail[row][col] = '*'
        col+=1

        #find the next row
        #using direction flag

        if dir_down:
            row += 1
        else:
            row -= 1

    #now we can construct the fill the rail matrix

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*')) and (index < len(cipher)): 
                rail[i][j] = cipher[index]
                index += 1

    # now read the matrix in the zig-zag manner to construct the resultant text

    result = []
    row, col = 0,0

    for i in range(len(cipher)):

        #check the direction flow

        if row == 0:
            dir_down = True
        else:
            dir_down = False

        #place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1 

        # find the next row using the direction flag

        if dir_down:
            row += 1
        else:
            row -= 1
    
    return ("".join(result))

# writing down the main logic 
def main():

    print (" \n WELCOME TO THE RAIL FENCE CIPHER HACKER \n")
    #Let the user provide the message that needs to be encrypted 
    print (" Please enter the message, that needs to be decrypted :")

    # Keep asking for inputs until we get the valid values 

    while True:    
        msg = input ('> ')
        if len(msg)> 0:
            break
        else :
            print (" Please enter the message ")
            continue
    
    best_score = 0
    best_key = None
    best_msg = ''

    for key in range(2,len(msg)-1): # since key value should be 1< key <len(msg)
        trans_msg = '' # Refreshing the value for each iteration
        trans_msg = decrypt_rail_fence(msg,key)
        # print(trans_msg)
        
        # score = word_score(trans_msg)
        # # print(key, score)

        # if score > best_score:

        #     best_score = score
        #     best_key = key
        #     best_msg = trans_msg

        if detectEnglish.isEnglish(trans_msg):

                # pyperclip.copy(trans_msg)
                print(f"Most likely message (Key = {key}):\n{trans_msg}")
    

# calling the function 

if __name__ == '__main__':    
    main()
