def autokey_encrypt(plaintext, key):
    plaintext = ''.join(plaintext.split()).lower()  # Remove spaces and convert to lowercase
    key_sequence = [key]  # Start with the numeric key
    ciphertext = []

    for i, char in enumerate(plaintext):
        if char.isalpha():  # Only process alphabetic characters
            shift = key_sequence[i] if i < len(key_sequence) else ord(plaintext[i - 1]) - ord('a')
            ciphertext.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            key_sequence.append(ord(ciphertext[-1]) - ord('a'))  # Update key sequence

    return ''.join(ciphertext)

def autokey_decrypt(ciphertext, key):
    key_sequence = [key]  # Start with the numeric key
    plaintext = []

    for i, char in enumerate(ciphertext):
        shift = key_sequence[i]
        p = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        plaintext.append(p)
        key_sequence.append(ord(p) - ord('a'))  # Update key sequence with decrypted character

    return ''.join(plaintext)

# Example usage
key = 7
plaintext = "the house is being sold tonight"

# Encrypt the message
ciphertext = autokey_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_text = autokey_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
