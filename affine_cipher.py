def affine_encrypt(text, a, b):
    encrypted_text = ''
    for char in text.lower():
        if char.isalpha():
            encrypted_char = chr((a * (ord(char) - 97) + b) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def affine_decrypt(text, a, b):
    a_inv = pow(a, -1, 26)
    decrypted_text = ''
    for char in text.lower():
        if char.isalpha():
            decrypted_char = chr((a_inv * (ord(char) - 97 - b)) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


# Example usage
a, b = 5, 8
plaintext = "hello world"
ciphertext = affine_encrypt(plaintext, a, b)
decrypted_text = affine_decrypt(ciphertext, a, b)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
