# Affine Cipher 

## Overview
The **Affine Cipher** is a type of monoalphabetic substitution cipher that uses a simple mathematical function to encrypt and decrypt messages.

Encryption formula:

E(x) = (a * x + b) mod m

Decryption formula:

D(x) = a^(-1) * (x - b) mod m

Where:
- x = position of the plaintext letter (0–25)
- a, b = keys (integers)
- m = size of the alphabet (26 for English)
- a^(-1) = modular inverse of a mod 26

---

## Key Rules
- `a` must be chosen such that gcd(a, 26) = 1 (i.e., `a` and 26 are coprime).
- `b` can be any integer between 0 and 25.

---

## Steps

**Encryption**
1. Convert each letter to a number (A=0, B=1, …, Z=25).
2. Apply E(x) = (a * x + b) mod 26.
3. Convert numbers back to letters.

**Decryption**
1. Compute modular inverse of a (denoted a^(-1)).
2. Apply D(x) = a^(-1) * (x - b) mod 26.
3. Convert numbers back to letters.

---

## Example
Keys: a=5, b=8  
Plaintext: HELLO

1. H(7) → (5×7+8) mod 26 = 17 → R  
2. E(4) → (5×4+8) mod 26 = 2 → C  
3. … and so on.

---

Ciphertext: **RCWWA**

---



```text
Plaintext  --> [ Convert to numbers ] --> Apply (a*x+b) mod 26 --> Ciphertext
Ciphertext --> [ Convert to numbers ] --> Apply a^-1(x-b) mod 26 --> Plaintext
```

---

## Python Notes
- Use `cryptomath.py` to find modular inverses.
- Program supports both encrypting and decrypting.
- Non-alphabetic characters (spaces, punctuation) remain unchanged.
