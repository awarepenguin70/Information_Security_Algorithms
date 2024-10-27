from Crypto.Cipher import AES
from Crypto.Util import Padding

# Key and message setup
key = b"0123456789ABCDEF"  # 16 bytes for AES-128
message = "Sensitive Information"

# Convert the message to bytes and pad it to a multiple of 16 bytes
message_bytes = message.encode()
padded_message = Padding.pad(message_bytes, AES.block_size)

# Encrypting the message
encrypt_cipher = AES.new(key, AES.MODE_ECB)
ciphertext = encrypt_cipher.encrypt(padded_message)
print("Ciphertext:", ciphertext.hex())

# Decrypting the ciphertext
decrypt_cipher = AES.new(key, AES.MODE_ECB)
decrypted_padded_message = decrypt_cipher.decrypt(ciphertext)
decrypted_message = Padding.unpad(decrypted_padded_message, AES.block_size).decode()
print("Decrypted message:", decrypted_message)
