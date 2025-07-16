# Find Missing Numbers

This Python script finds all missing numbers in a given list that should contain a continuous range from 1 to the maximum value in the list.

## How It Works

- The user is prompted to input a list of numbers separated by commas (e.g., `1,2,4,6,7`).
- The script converts the input into a list of integers.
- It then checks for any numbers missing in the sequence from 1 to the maximum number in the list.
- The missing numbers are printed as output.

## Usage

1. Run the script:
    ```
    python find_missing_number.py
    ```
2. When prompted, enter a list of numbers separated by commas:
    ```
    input the list of numbers here : 1,2,4,6,7
    ```
3. The script will output:
    ```
    Here is the list of the missing numbers list : [3, 5]
    ```

## Example

**Input:**
```
1,2,4,6,7
```
**Output:**
```
Here is the list of the missing numbers list : [3, 5]
```

## Notes

- The script expects numbers separated by commas, with no missing values at the start or end of the range.
- Handles invalid input gracefully by printing the error message.