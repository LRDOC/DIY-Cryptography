'''
December 11th, 2023
CS5002 Final Project
Hill Cipher encrypter/decrypter
A polygraphic substitution cipher based on linear algebra.
'''

import numpy as np
import sympy

key_matrix_saver = 'key_matrix.npy'

def save_key_matrix(key_matrix):
    '''
    This function saves the key matrix to a file.
    Parameters: key_matrix
    Returns: None
    '''
    with open(key_matrix_saver, 'wb') as f:
        np.save(f, key_matrix)

def load_key_matrix():
    '''
    This function loads the key matrix from a file.
    Parameters: None
    Returns: The key matrix
    '''
    with open (key_matrix_saver, 'rb') as key_file:
        return np.load(key_file)

def generate_key_matrix(size):
    '''
    This function generates a random key matrix of a given size.
    Parameters: size
    Returns: The key matrix
    '''
    while True:
        matrix = np.random.randint(0, 26, size=(size, size))
        if int(sympy.Matrix(matrix).det()) % 26 != 0 and np.gcd(int(sympy.Matrix(matrix).det()), 26) == 1: # Check if determinant of key is coprime to 26
            save_key_matrix(matrix)
            return matrix

def matrix_modulo(message_matrix, key_matrix, mod = 26):
    '''
    This function performs a modulo operation on a matrix. This is how the Hill cipher works.
    Parameters: message_matrix, key_matrix, mod
    Returns: The result matrix
    '''
    result_matrix = np.dot(message_matrix, key_matrix) % mod #Np.dot() performs matrix multiplication making my for loop obsolete
    return result_matrix
    
def encrypt_hill(message, key_matrix):
    '''
    This function encrypts a message using the Hill cipher.
    Parameters: message, key
    Returns: The encrypted message
    '''
    message = message.upper().replace(' ', '|')  # Replace spaces with '|'
    encrypted_message = ''
    message_matrix = []

    for char in message: # Iterate over characters in message
        if char.isalpha():
            message_matrix.append(ord(char) - 65) # Convert character to number and add to message matrix
        elif char == '|':
            message_matrix.append(26)  # Use 26 to represent '|'

        if len(message_matrix) == key_matrix.shape[0]: # If the message matrix is full, encrypt it
            block = np.array(message_matrix).reshape(-1, key_matrix.shape[0]) # Reshape to a matrix
            encrypted_block = matrix_modulo(block, key_matrix, mod=27)  # Modulus is now 27
            for num in encrypted_block.flatten(): # Flatten the matrix and add the characters to the encrypted message
                if num < 26:
                    encrypted_message += chr(num + 65) # Convert the number to a character
                else:
                    encrypted_message += '|' # Replace 26 with '|'
            message_matrix = []

    # Handle padding for the last block, if necessary
    if message_matrix:
        while len(message_matrix) < key_matrix.shape[0]:
            message_matrix.append(26)  # Pad with '|'
        block = np.array(message_matrix).reshape(-1, key_matrix.shape[0]) # Reshape to a matrix
        encrypted_block = matrix_modulo(block, key_matrix, mod=27) # encrypt the block, matrix_modulo() handles the padding by doing the modulo operation
        for num in encrypted_block.flatten(): # Flatten the matrix and add the characters to the encrypted message | Flatten() returns a 1D array
            if num < 26:
                encrypted_message += chr(num + 65) # Convert the number to a character
            else:
                encrypted_message += '|' # Replace 26 with '|'

    return encrypted_message

def decrypt_hill(encrypted_message, key_matrix):
    '''
    This function decrypts a ciphertext
    using the Hill cipher given a key.
    Parameters: ciphertext, key
    Returns: The decrypted message
    '''
    inverse_key_matrix = np.array(sympy.Matrix(key_matrix).inv_mod(27).tolist(), dtype=int)  # Modulus is now 27 bc |and padding
    decrypted_message = ''
    encrypted_matrix = []

    for char in encrypted_message: # Iterate over characters in encrypted message
        if char.isalpha():
            encrypted_matrix.append(ord(char) - 65) # Convert character to number and add to encrypted matrix
        elif char == '|':
            encrypted_matrix.append(26)

        if len(encrypted_matrix) == key_matrix.shape[0]:
            block = np.array(encrypted_matrix).reshape(-1, key_matrix.shape[0]) # Reshape to a matrix
            decrypted_block = matrix_modulo(block, inverse_key_matrix, mod=27) # Modulus is now 27 
            for num in decrypted_block.flatten(): # Flatten the matrix and add the characters to the decrypted message
                if num < 26:
                    decrypted_message += chr(num + 65)
                else:
                    decrypted_message += ' '  # Replace '|' with a space
            encrypted_matrix = []

    # Remove any padding '|' characters
    decrypted_message = decrypted_message.replace('|', ' ').rstrip('X')

    return decrypted_message

def main():
    key_matrix_size = 2 # Size of key matrix bc 2x2 is the smallest invertible matrix | This matrix will reshape when encrypting/decrypting
    
    #VAN DO NOT DELETE THIS 5 LINES OF CODE
    # Hahaha, noted --Van
    try:
        key_matrix = load_key_matrix() # Load key matrix from file
    except FileNotFoundError:
        key_matrix = generate_key_matrix(key_matrix_size) # Generate key matrix
        save_key_matrix(key_matrix)
    
    choice = input("Do you want to (E)ncrypt, (D)ecrypt:\n>>> ").upper()

    #User Input
    if choice == 'E':
        message = input("Enter your message you want to encrypt:\n>>> ")
        if len(message) % key_matrix_size != 0:
            message += 'X' * (key_matrix_size - (len(message) % key_matrix_size)) # Add X's to make message length divisible by key matrix size
        encrypted_message = encrypt_hill(message, key_matrix) # Encrypt message
        print(f"Encrypted Message: {encrypted_message}")
        
    elif choice == 'D':
        encrypted_message = input("Enter your message you want to decrypt:\n>>> ") # Get encrypted message from user
        decrypted_message = decrypt_hill(encrypted_message, key_matrix)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid Input")
        main()
    
if __name__ == "__main__":
    main()