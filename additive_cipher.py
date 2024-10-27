# Function to encrypt using Additive Cipher
def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            encrypted += chr((ord(char) - 97 + key) % 26 + 97)  # For lowercase letters
    return encrypted

# Function to decrypt using Additive Cipher
def decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted += chr((ord(char) - 97 - key) % 26 + 97)  # For lowercase letters
    return decrypted

# Example usage
message = "I am learning information security"  # Original message
key = 20

encrypted_message = encrypt(message, key)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
