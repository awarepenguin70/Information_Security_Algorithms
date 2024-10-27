def custom_hash(input_string):
    # Initial hash value
    hash_value = 5381

    for char in input_string:
        # Update hash value
        hash_value = (hash_value * 33) ^ ord(char)  # Using XOR for bit mixing
        hash_value &= 0xFFFFFFFF  # Keep within 32-bit range

    return hash_value

# Example usage
input_string = "Hello, World!"
hash_value = custom_hash(input_string)
print("Hash value:", hash_value)
