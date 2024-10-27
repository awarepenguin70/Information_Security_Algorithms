from itertools import cycle
import string

def vigenere_encrypt(plaintext, key):
    plaintext = ''.join(plaintext.split()).lower()  # Remove spaces and convert to lowercase
    key = cycle(key.lower())  # Repeat the key
    ciphertext = ''.join(chr((ord(p) - ord('a') + ord(k) - ord('a')) % 26 + ord('a'))
                         for p, k in zip(plaintext, key))
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = cycle(key.lower())  # Repeat the key
    plaintext = ''.join(chr((ord(c) - ord(k) + 26) % 26 + ord('a'))
                        for c, k in zip(ciphertext, key))
    return plaintext

# Example usage
key = "dollars"
plaintext = "the house is being sold tonight"

# Encrypt the message
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = vigenere_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
