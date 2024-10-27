def affine_encrypt(text, a, b):
    return ''.join(chr((a * (ord(c) - 97) + b) % 26 + 97) if c.isalpha() else c for c in text.lower())

def affine_decrypt(text, a, b):
    a_inv = pow(a, -1, 26)
    return ''.join(chr((a_inv * (ord(c) - 97 - b)) % 26 + 97) if c.isalpha() else c for c in text.lower())

# Example usage
a, b = 5, 8
plaintext = "hello world"
ciphertext = affine_encrypt(plaintext, a, b)
decrypted_text = affine_decrypt(ciphertext, a, b)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
