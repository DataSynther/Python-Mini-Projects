# Function to find Longest Common Sub-string
from difflib import SequenceMatcher
def longest_common_substring(s1, s2):
    """
    Find the longest common substring between two strings.
    
    Args:
    s1 (str): First string.
    s2 (str): Second string.
    
    Returns:
    str: The longest common substring.
    """
    # initialize SequenceMatcher object with 
    # input string
    matcher = SequenceMatcher(None, s1, s2)

    # find the longest match
    #output will be like match (a= 0, b = 0, size = 5 )
    match = matcher.find_longest_match(0, len(s1), 0, len(s2))


    if match.size!=0:
        # return the longest common substring
        # match.a is the starting index of the match in s1
        # match.size is the length of the match

        return s1[match.a: match.a + match.size]
    else:
        print("No common substring found")
        return None
    
# Calculate the percentage similarity between two strings
def percentage_similarity(s1, s2):
    """
    Calculate the percentage similarity between two strings.
    
    Args:
    s1 (str): First string.
    s2 (str): Second string.
    
    Returns:
    float: Percentage similarity between the two strings.
    """
    matcher = SequenceMatcher(None, s1, s2)
    return matcher.ratio() * 100

# String reverser
def string_reverser(s):
    """
    Reverse a given string.
    
    Args:
    s (str): The string to reverse.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]

## Example usage
if __name__ == "__main__":
    str1 = "Hello, this is a sample string."
    str2 = "This is a sample string for testing."

    # Find the longest common substring
    lcs = longest_common_substring(str1, str2)
    print(f"Longest Common Substring: {lcs}")

    # Calculate the percentage similarity
    similarity = percentage_similarity(str1, str2)
    print(f"Percentage Similarity: {similarity:.2f}%")

    # Reverse a string
    reversed_str = string_reverser(str1)
    print (f"Reversed String: {reversed_str}")
    reversed_str2 = string_reverser(str2)
    print (f"Reversed String 2: {reversed_str2}")   