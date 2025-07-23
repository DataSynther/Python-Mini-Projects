
# Caesar Cipher Hacker

This program can hack messages encrypted with the Caesar cipher, even if the encryption key is unknown.  
It performs a **brute-force attack** by trying all 66 possible keys (based on the defined character set) and attempts to decrypt the message.

### 🔐 What is Caesar Cipher?
The Caesar Cipher is a simple shift cipher that uses addition and subtraction to encrypt and decrypt letters.  
More info: [Wikipedia - Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

### 🧠 How It Works
- The program takes an **encrypted message** from the user.
- It attempts all possible decryption keys by shifting letters back one-by-one.
- It uses the `langdetect` library to check if the resulting text is valid English.
- As soon as a valid English message is detected, it displays the decrypted message and stops further testing.

### 🧩 Symbol Set
The program works with the following characters:  
`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`

### 📦 Requirements
- Python 3.x
- `langdetect` module

To install required module:

```bash
pip install langdetect
```

### ▶️ Usage

```bash
python caesar_cipher_hacker.py
```

Sample Interaction:
```
WELCOME TO CAESAR CIPHER HACKER
Enter the encrypted Caesar Cipher message to hack.
> Khoor Zruog
Decoding Completed

Key #3: Hello World


Thanks for using this! See you next time!
```

---
© 2025 Caesar Cipher Toolkit
