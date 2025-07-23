"""
This program can hack messages encrypted with the Caesar cipher if someone doesn't know the key.
Since there are only 26 possible keys for the caesar cipher, so computer can easily try all the 
possible decryption keys and display the results to the user.

In cryptography, we call this technique a brute-force attack.

"""

from langdetect import detect

print ("  WELCOME TO CAESAR CIPHER HACKER ")
#Let the user specify the message that needs to ne hacked:
print ('Enter the encrypted Caeser Cipher message to hack.')
msg = input ('> ')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


# Loop through every possible key:
for key in range(len(SYMBOLS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared:
    translated = ''

    # The rest of the program is almost the same as the Caesar program:

    # Loop through each symbol in message:
    for symbol in msg:
        if symbol in SYMBOLS:
            
            #Get the encrypted (or decrypted) number for this symbol
            num = SYMBOLS.find(symbol)
            num = num-key

            #Handle the wrap around if number is larger than the length of SYMBOLS (or less than zero)
            if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)
            elif num < 0:
                num = num + len(SYMBOLS)
            
            #Add encrypted/ decrypted number's symbol to translated:
            translated = translated + SYMBOLS [num]

        else:
            #Just add the symbol without encrypting/decrypting
            translated = translated + symbol
    
    # Display the key being tested, along with the decrypted text:
    # print ('decoding ongoing ............. Trying with ......................')
    # print ('Key #{}:{}'.format(key,translated))

    # Detect is the translated text is english, if yes we stop the program
    if detect(translated)  == 'en':
        # Prints that we have found the original message 
        print (" \n Decoding Completed \n  ")
        print ('\n Key #{}:{}\n '.format(key,translated))
        print (' \n\n Thanks for using this ! See you next time !\n\n')
        break 

