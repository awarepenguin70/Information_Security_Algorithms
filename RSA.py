# RSA parameters
n = 323
e = 5
d = 173

def rsa_encrypt(message):
    # Convert each character to its ASCII value and encrypt it
    ciphertext = [(ord(char) ** e) % n for char in message]
    return ciphertext

def rsa_decrypt(ciphertext):
    # Decrypt each number back to characters
    decrypted_message = ''.join(chr((num ** d) % n) for num in ciphertext)
    return decrypted_message

# Main execution
original_message = "Cryptographic Protocols"
ciphertext = rsa_encrypt(original_message)
print("Ciphertext:", ciphertext)

decrypted_message = rsa_decrypt(ciphertext)
print("Decrypted message:", decrypted_message)
