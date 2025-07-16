## In this part we will learn how to remove cuss words from a text file using Python utilizing betterprofanity library.
from better_profanity import profanity
def remove_cuss_words(text):
    """
    This function takes a string input and removes any cuss words from it.
    
    Parameters:
    text (str): The input string from which cuss words need to be removed.
    
    Returns:
    str: The cleaned string with cuss words removed.
    """
    return profanity.censor(text)

def main():
    # Example usage
    text = "This is a damn example with some cuss words."
    cleaned_text = remove_cuss_words(text)
    print("Original Text:", text)
    print("Cleaned Text:", cleaned_text)

if __name__ == "__main__":
    main()
