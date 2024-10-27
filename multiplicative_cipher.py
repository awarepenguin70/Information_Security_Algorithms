# Function to compute modular inverse of key
def mod_inverse(key, mod):
    return pow(key, -1, mod)

# Function to encrypt using Multiplicative Cipher
def encrypt_multiplicative(plaintext, key):
    plaintext = plaintext.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            encrypted += chr(((ord(char) - 97) * key) % 26 + 97)  # Apply the encryption formula
    return encrypted

# Function to decrypt using Multiplicative Cipher
def decrypt_multiplicative(ciphertext, key):
    decrypted = ""
    mod_inv = mod_inverse(key, 26)  # Get the modular inverse of the key
    if mod_inv is None:
        return "No modular inverse exists, decryption not possible with this key"

    for char in ciphertext:
        if char.isalpha():
            decrypted += chr(((ord(char) - 97) * mod_inv) % 26 + 97)  # Apply the decryption formula
    return decrypted

# Example usage
message = "I am learning information security"  # Original message
key = 7  # Key must be coprime with 26

encrypted_message = encrypt_multiplicative(message, key)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt_multiplicative(encrypted_message, key)
print("Decrypted:", decrypted_message)
