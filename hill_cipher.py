def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_cipher_encrypt(message, key_matrix):
    # Prepare message in uppercase and remove spaces
    message = message.replace(" ", "").upper()

    # Ensure message has even length by padding with 'X' if needed
    if len(message) % 2 != 0:
        message += 'X'

    # Convert message to numbers
    message_numbers = text_to_numbers(message)

    # Encrypt in pairs
    ciphertext_numbers = []
    for i in range(0, len(message_numbers), 2):
        # Get the pairs
        pair = message_numbers[i:i+2]

        # Matrix multiplication manually with key matrix
        c1 = (key_matrix[0][0] * pair[0] + key_matrix[0][1] * pair[1]) % 26
        c2 = (key_matrix[1][0] * pair[0] + key_matrix[1][1] * pair[1]) % 26

        # Append the results to ciphertext numbers
        ciphertext_numbers.extend([c1, c2])

    # Convert numbers back to text
    ciphertext = numbers_to_text(ciphertext_numbers)
    return ciphertext

# Key matrix as a list of lists
key_matrix = [[3, 3], [2, 7]]

# Message to encrypt
message = "We live in an insecure world"

# Encrypt the message
ciphertext = hill_cipher_encrypt(message, key_matrix)
print("Ciphertext:", ciphertext)
