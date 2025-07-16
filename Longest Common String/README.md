# Longest Common Substring & String Similarity Utilities

This Python script provides utilities for:
- Finding the longest common substring between two strings
- Calculating the percentage similarity between two strings
- Reversing a string

## Features

- **Longest Common Substring:** Uses Python's `difflib.SequenceMatcher` to find the longest sequence of matching characters between two strings.
- **Percentage Similarity:** Calculates how similar two strings are as a percentage.
- **String Reverser:** Reverses any given string.

## Requirements

- Python 3.x (no external dependencies required)

## Usage

1. Edit the script to set your input strings, or use the provided example.
2. Run the script:
    ```
    python longest_sequence_matcher.py
    ```

## Example

**Input:**
```python
str1 = "Hello, this is a sample string."
str2 = "This is a sample string for testing."
```

**Output:**
```
Longest Common Substring:  is a sample string
Percentage Similarity: 56.41%
Reversed String: .gnirts elpmas a si siht ,olleH
Reversed String 2: .gnitset rof gnirts elpmas a si sihT
```

## Functions

- `longest_common_substring(s1, s2)`: Returns the longest common substring between `s1` and `s2`.
- `percentage_similarity(s1, s2)`: Returns the similarity percentage between `s1` and `s2`.
- `string_reverser(s)`: Returns the reversed version of string `s`.

## Notes

- If no common substring is found, the function prints a message and returns `None`.
- The script is self-contained and ready to use for string