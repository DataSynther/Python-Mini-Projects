"""
Brute-Force & Word Pattern Analysis (Substitution Cipher)

- Brute-force: test all keys → impractical (too many).
- Optimization: analyze ciphertext to reduce possible keys.
- Cipherwords: groups of letters (like words) in ciphertext.
- Cipherletters: individual encrypted letters.
- Key property: each plaintext letter ↔ one unique cipherletter; spaces unchanged.
- Result: plaintext & ciphertext share same word/letter patterns.
- Example:
    - MISSISSIPPI SPILL → RJBBJBBJXXJ BXJHH
    - Word lengths & repeated letters match.
- Approach:
    - Match cipherwords to dictionary words with same pattern.
    - Use matches to deduce letter mappings.
    - Enough mappings → decrypt entire message.

"""
# Importing the necessary packages and user defined py functions
import os, re, copy, pyperclip, sim_subs_encrypt, wordPatterns, makeWordPatterns, string

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWZYZ'
nonLettersOrSpacePattern =  re.compile ('[^A-Z\s]')

def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping:
    return {ch: [] for ch in string.ascii_uppercase}

def addLettersToMapping(letterMapping, cipherword, candidate):
    
    """
    The letterMapping parameter takes a dictionary value that 
    stores a cipherletter mapping, which is copied by the function.
    The cipherword parameter is a string value of the ciphertext word.
    The candidate parameter is a possible English word that the cipherword could decrypt to

    This function adds the letters in the candidate as potential
    decryption letters for the cipherletters in the cipherletter mapping
    
    """
    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])

def intersectMappings(mapA, mapB):

    """
    To intersect two maps, create a blank map and then add only the potential
    decryption letters if they exist in BOTH maps :
    
    """

    intersectedMapping = getBlankCipherletterMapping()

    for letter in LETTERS:
        # An empty list means "any letter is possible". In this case just 
        # copy the other map entirely:

        if mapA[letter] == []:
            intersectMappings[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectMappings[letter] = 
