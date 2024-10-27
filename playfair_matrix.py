def create_playfair_matrix(key):
    # Remove duplicates and fill with the rest of the alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Combine I and J
    key = ''.join(dict.fromkeys(key))  # Remove duplicates from the key
    matrix_string = key + ''.join(c for c in alphabet if c not in key)

    # Create the 5x5 matrix
    matrix = [list(matrix_string[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def prepare_message(message):
    message = ''.join(message.split()).upper()  # Remove spaces and convert to uppercase
    prepared = []

    i = 0
    while i < len(message):
        if i == len(message) - 1:  # Single character left
            prepared.append(message[i] + 'X')
            break
        if message[i] == message[i + 1]:  # Same letters
            prepared.append(message[i] + 'X')
            i += 1
        else:
            prepared.append(message[i] + message[i + 1])
            i += 2

    return prepared

def encrypt_playfair(prepared_message, matrix):
    # Create a position mapping for each letter in the matrix
    pos = {char: (i, j) for i, row in enumerate(matrix) for j, char in enumerate(row)}
    cipher_text = []

    for digraph in prepared_message:
        row1, col1 = pos[digraph[0]]
        row2, col2 = pos[digraph[1]]

        # Same row
        if row1 == row2:
            cipher_text.append(matrix[row1][(col1 + 1) % 5])
            cipher_text.append(matrix[row2][(col2 + 1) % 5])
        # Same column
        elif col1 == col2:
            cipher_text.append(matrix[(row1 + 1) % 5][col1])
            cipher_text.append(matrix[(row2 + 1) % 5][col2])
        # Rectangle swap
        else:
            cipher_text.append(matrix[row1][col2])
            cipher_text.append(matrix[row2][col1])

    return ''.join(cipher_text)

# Example usage
key = "GUIDANCE"
message = "The key is hidden under the door pad"

# Create the Playfair matrix
playfair_matrix = create_playfair_matrix(key)

# Prepare the message
prepared_message = prepare_message(message)

# Encrypt the message
ciphertext = encrypt_playfair(prepared_message, playfair_matrix)
print("Ciphertext:", ciphertext)
