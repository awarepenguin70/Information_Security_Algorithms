import random

# ElGamal parameters
p = 7919
g = 2
h = 6465
x = 2999

def elgamal_encrypt(message):
    ciphertext = []
    for char in message:
        y = random.randint(1, p - 2)  # Random integer y
        c1 = pow(g, y, p)              # c1 = g^y mod p
        s = pow(h, y, p)               # s = h^y mod p
        c2 = (ord(char) * s) % p       # c2 = (m * s) mod p
        ciphertext.append((c1, c2))
    return ciphertext

def elgamal_decrypt(ciphertext):
    decrypted_message = ''
    for c1, c2 in ciphertext:
        s = pow(c1, x, p)              # s = c1^x mod p
        s_inv = pow(s, p - 2, p)       # s^-1 mod p (using Fermat's Little Theorem)
        m = (c2 * s_inv) % p           # m = (c2 * s^-1) mod p
        decrypted_message += chr(m)
    return decrypted_message

# Main execution
original_message = "Asymmetric Algorithms"
ciphertext = elgamal_encrypt(original_message)
print("Ciphertext:", ciphertext)

decrypted_message = elgamal_decrypt(ciphertext)
print("Decrypted message:", decrypted_message)
