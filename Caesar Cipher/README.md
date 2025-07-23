
# Caesar Cipher

The Caesar Cipher is a simple substitution cipher that shifts letters in the alphabet by a fixed number of positions. It uses addition and subtraction to encrypt and decrypt letters.

More info: [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)

## Features

- Encrypt or decrypt a message based on a user-specified key.
- Works only on uppercase letters A–Z by default.
- Ignores characters not in the supported alphabet (they are added unchanged).
- Copies the result to the clipboard (requires `pyperclip` module).

## How It Works

- You choose whether to encrypt or decrypt.
- You provide a key (a number between 0 and 25).
- You input a message in uppercase.
- Each character is shifted by the key amount to produce the encrypted/decrypted message.
- Non-alphabet symbols are not modified.

## Example

If your message is `HELLO` and the key is `2`:
- Encrypting will return: `JGNNQ`
- Decrypting `JGNNQ` with the same key will return: `HELLO`

## Dependencies

- `pyperclip` (optional, for copying results to clipboard)

Install it using pip if not already installed:

```bash
pip install pyperclip
```

## Code Overview

- `symbols`: Defines the set of characters supported (`A–Z`).
- `mode`: Encrypt or Decrypt.
- `key`: Determines how far to shift each letter.
- `translated`: The final encrypted/decrypted message.
- Clipboard support is provided using `pyperclip`.

## Limitations

- No automatic decryption (brute-force or frequency analysis).


