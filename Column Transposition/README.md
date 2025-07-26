# Columnar Transposition Cipher (Encryption Only)

This script performs **Columnar Transposition Cipher encryption** using a given keyword.

### 🔐 How It Works

Columnar Transposition involves writing the plaintext in rows and reading it column by column.

### ✍️ Steps to Encrypt

1. Count the characters in the message and determine the key (length of keyword).
2. Draw a row with boxes equal to the key (i.e. if key = 8, columns = 8).
3. Fill the boxes left to right, one character per box.
4. On running out of space, move to the next row.
5. Shade any leftover empty boxes.
6. Read the columns top to bottom, ordered by alphabetical order of the keyword.

###
**Note**: Make sure you have `pyperclip` installed to copy output to clipboard.