from Crypto.Cipher import DES
from Crypto.Util import Padding

# Key and message setup
key = b"A1B2C3D4"  # 8-byte key for DES
message = "Confidential Data"

# Convert the message to bytes and pad it to a multiple of 8 bytes
message_bytes = message.encode()
padded_message = Padding.pad(message_bytes, DES.block_size)

# Encrypting the message
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(padded_message)
print("Ciphertext:", ciphertext.hex())

# Decrypting the ciphertext
decrypted_padded_message = cipher.decrypt(ciphertext)
decrypted_message = Padding.unpad(decrypted_padded_message, DES.block_size).decode()
print("Decrypted message:", decrypted_message)
