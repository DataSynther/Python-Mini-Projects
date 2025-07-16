# Word Anagram Grouper

This Python script groups a list of words into sets of anagrams.

## How It Works

- The script defines a function `group_anagrams` that takes a list of words.
- It sorts the letters in each word and uses this as a key to group words that are anagrams of each other.
- The grouped anagrams are returned as a collection of lists.

## Usage

1. Add your list of words to the `words` variable in the script.
2. Run the script:
    ```
    python word_anagram.py
    ```
3. The script will print the grouped anagrams.

## Example

**Input:**
```python
words = ["tea", "eat", "bat", "ate", "arc", "car"]
```

**Output:**
```
dict_values([['tea', 'eat', 'ate'], ['bat'], ['arc', 'car']])
```

## Notes

- The script uses Python's `collections.defaultdict` for grouping.
- Handles exceptions gracefully and prints