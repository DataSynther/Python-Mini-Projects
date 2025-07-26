# Columnar Transposition Cipher - Decryption

This program implements **decryption** for the Columnar Transposition Cipher.  

## Decryption Steps:

1. **Determine the Grid:**
   - Calculate the number of columns:  
     `num_of_columns = ceil(len(message) / key)`  
   - The number of rows is equal to the key.

2. **Shade Extra Boxes:**
   - Calculate shaded (unused) boxes:  
     `(columns * rows) - len(ciphertext)`  
   - Shade these boxes from the bottom of the rightmost column.

3. **Fill the Grid:**
   - Write the ciphertext column by column (skipping shaded boxes).

4. **Read Row-wise:**
   - Finally, read the grid row by row to reconstruct the plaintext.

> Using an incorrect key results in garbage output even if the procedure is followed correctly.

## How It Works

- The program asks for the ciphertext and a key.
- It reconstructs the plaintext based on the columnar transposition algorithm.
- The final plaintext is displayed and also copied to the clipboard (if `pyperclip` is installed).

## Usage

Run the program:

```bash
python decrypt_columnar.py
```

Follow the prompts to provide:
- The encrypted message.
- The numeric key.

---
