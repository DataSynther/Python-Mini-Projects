# Group Elements of Same Indices

This Python script groups elements from multiple lists by their indices, effectively transposing a list of lists.

## How It Works

- The function `group_elements(lst)` takes a list of lists as input.
- It uses `zip(*lst)` to group elements at the same index from each sublist.
- The result is a list of lists, where each inner list contains elements from the same index of the original sublists.

## Usage

1. Add your list of lists to the `li` variable in the script.
2. Run the script:
    ```
    python group_elements.py
    ```
3. The script will print the original list and the grouped (transposed) list.

## Example

**Input:**
```python
li = [[1, 4, 5], [4, 6, 8], [8, 3, 10], [25, 30, 80]]
```

**Output:**
```
Original list : [[1, 4, 5], [4, 6, 8], [8, 3, 10], [25, 30, 80]]
Index pairs list : [[1, 4, 8, 25], [4, 6, 3, 30], [5, 8, 10, 80]]
```

## Notes

- The script handles exceptions and prints any errors encountered.
- Useful for transposing matrices or grouping data by