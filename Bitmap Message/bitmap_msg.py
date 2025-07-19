'''
This program uses a multiline string as a bitmap, a 2D image with only two possible colors for each pixel,
to determine how it should display a message from the user. In this bitmap, space characters represent an 
empty space, and all other characters are replaced by characters in the user’s message.

'''

import sys

try:
    # Read the ascii art from a file
    with open("ascii_art.txt", "r") as f:
        ascii_art = f.read()    

    # print(ascii_art)  # Displays the full content of the file

except FileNotFoundError:
    print("The ascii_art.txt file does not exist. Please generate it first using the bitmap_txt_generator.py script.")

## Define ASCII characters for intensity mapping
try:
    ASCII_CHARS = "@%#*+=-:. "  # Darkest to lightest

    def get_intensity(char):
        """Returns an index representing intensity of a char in the ASCII_CHARS list."""
        try:
            return ASCII_CHARS.index(char)
        except ValueError:
            return len(ASCII_CHARS) - 1 # Assume lightest if not found
except Exception as e:
    print(f"An error occurred while setting up ASCII characters: {e}")
    sys.exit(1)

## Display a message in the bitmap

try:

    print ("Welcome to the Bitmap Message Program!" \
    "\nYou can display a message using the bitmap art generated from an image.\n" \
    "Please enter your message (100 characters max):")
    
    user_message = input('> ').strip()
    
    if len(user_message) > 100:
        print("Message too long! Please limit your message to 100 characters.")
    elif len(user_message) == 0:
        print("No message entered. Exiting the program.")
        sys.exit(0)
    else:
        #Loop over each line of the ascii art
        for line in ascii_art.splitlines():
            #loop over each character in the line
            for i, bit in enumerate(line):
                #if the character is a space, print it
                if bit == ' ':
                    print(' ', end='')
                else:
                    #print the corresponding character from the user message
                    char_to_print = user_message[i % len(user_message)]
                    intensity = get_intensity(bit)

                    # Apply styling based on intensity (darkest = 0, lightest = 9)
                    if intensity < 3:
                        # Dark: bold look (uppercase)
                        print(char_to_print.upper(), end='')
                    elif intensity < 6:
                        # Medium: as is
                        print(char_to_print, end='')
                    else:
                        # Light: faded (lowercase or dot)
                        print(char_to_print.lower() if char_to_print.isalpha() else '.', end='')

            print()  # Print a newline after each line of ASCII art
        print("\nMessage displayed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")