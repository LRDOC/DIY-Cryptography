'''
December 11th, 2023
CS5002 Final Project
Baconian Cipher encrypter/decrypter
'''
# I chose this cipher because of the name -Van

# Dictionary to encode the alphabet with the Baconian cipher's 'A'/'B' sequences
bacon_dict = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
    'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
    'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
    'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
    'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
    'Z': 'BBAAB'
}

# Inverse dictionary to decode the sequences back to the alphabet
inv_bacon_dict = {v: k for k, v in bacon_dict.items()}

def baconian_encrypt(message):
    '''Function to encrypt a message using the Baconian cipher.
    Parameters: Message to be encrypted
    Returns: The encrypted message
    '''
    encrypted_message = ''
    for char in message.upper():
        if char in bacon_dict:
            encrypted_message += bacon_dict[char]
        else:
            encrypted_message += char  # Non-alphabetic characters are kept as they are
    return encrypted_message

def encrypt_file(input_file_path, output_file_path): # A useful function for future refactoring!
    '''This function reads a plaintext file, encrypts its content using
    the Baconian cipher, and writes the encrypted text to a new file.
    '''
    with open(input_file_path, 'r') as file:
        plaintext = file.read()
    
    encrypted_text = baconian_encrypt(plaintext)

    with open(output_file_path, 'w') as file:
        file.write(encrypted_text)

    print(f"Encrypted text written to {output_file_path}")

def baconian_decrypt(encrypted_message):
    '''Function to decrypt a message encoded with the Baconian cipher.
    Parameters: encrypted message to be decrypted.
    Returns: The now readable decrypted message.
    '''
    decrypted_message = ''
    for i in range(0, len(encrypted_message), 5):  # Process every 5 characters
        seq = encrypted_message[i:i+5]
        if seq in inv_bacon_dict:  # Check if the sequence is in the dictionary
            decrypted_message += inv_bacon_dict[seq]
        else:
            decrypted_message += '?'  # Place a ? for sequences/chars that don't match
    return decrypted_message

def read_message_from_file(file_path):
    '''This function opens a file to be read.
    Parameters: The file (file_path) 
    Returns: None
    '''
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("File not found. Try again.")
        return None

def get_user_input_or_file():
    '''This function gets user input as a message or a separate file.
    Parameters: None
    Returns: The message/file_path being used.
    '''
    choice = input("Enter message directly or specify a file? (Type 'M' for message, 'F' for file):\n>>> ").upper()
    if choice == 'F':
        file_path = input("Enter the full path of the .txt file:\n>>> ")
        return read_message_from_file(file_path)
    else:
        return input("Enter your message:\n>>> ")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D):\n>>> ").upper()

    message = get_user_input_or_file()
    if message is None:
        return

    if choice == 'E':
        encrypted_message = baconian_encrypt(message)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = baconian_decrypt(message.replace(' ', ''))  # Remove spaces for decryption
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid option. Please choose 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
