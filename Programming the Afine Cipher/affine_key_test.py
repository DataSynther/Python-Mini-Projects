# This program proves that the keyspace of the affine cipher is limited
# to less than len(symbols)^2

import affine_cipher_encryption,cryptomath

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2,80):
    key = keyA * len (affine_cipher_encryption.symbols) + 1

    if cryptomath.gcd(keyA, len(affine_cipher_encryption.symbols)) == 1 :
        print(keyA, affine_cipher_encryption.encryptMessage(key, message))