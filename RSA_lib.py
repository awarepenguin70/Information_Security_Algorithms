# RSA Encryption and Decryption Example
# To run this code, install the following library:
# pip install rsa

import rsa

# Step 1: Generate RSA keys (public and private)
public_key, private_key = rsa.newkeys(512)

# Step 2: Encrypt a message with the public key
message = "Hello, this is a secret message!"
encrypted_message = rsa.encrypt(message.encode(), public_key)
print("Encrypted message:", encrypted_message)

# Step 3: Decrypt the message with the private key
decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
print("Decrypted message:", decrypted_message)
