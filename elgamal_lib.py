# ElGamal Encryption and Decryption Example
# To run this code, install the following library:
# pip install elgamal

import elgamal

# Step 1: Generate ElGamal keys (public and private)
key = elgamal.generate_keys()
public_key = key["publicKey"]
private_key = key["privateKey"]

# Step 2: Define a message to encrypt
message = "Hello, this is a secret message!"

# Convert the message to an integer for encryption (ElGamal works with integers)
message_as_int = int.from_bytes(message.encode(), "big")

# Step 3: Encrypt the message using the public key
ciphertext = public_key.encrypt(message_as_int)
print("Encrypted message:", ciphertext)

# Step 4: Decrypt the message using the private key
decrypted_message_int = private_key.decrypt(ciphertext)
decrypted_message = decrypted_message_int.to_bytes((decrypted_message_int.bit_length() + 7) // 8, "big").decode()
print("Decrypted message:", decrypted_message)
