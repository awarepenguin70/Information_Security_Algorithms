from Crypto.Random import get_random_bytes
from Crypto.Util import number

p, g, h, x = 7919, 2, 6465, 2999

def elgamal_encrypt(msg):
    return [(c1 := pow(g, y := number.getRandomRange(1, p - 1), p), (ord(c) * pow(h, y, p)) % p) for c in msg]

def elgamal_decrypt(ciphertext):
    return ''.join(chr((c2 * pow(pow(c1, x, p), p - 2, p)) % p) for c1, c2 in ciphertext)

# Main execution
original_message = "Asymmetric Algorithms"
ciphertext = elgamal_encrypt(original_message)
print("Ciphertext:", ciphertext)
print("Decrypted message:", elgamal_decrypt(ciphertext))
