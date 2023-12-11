'''
December 11th, 2023
CS5002 Final Project
Caesar Cipher encrypter/decrypter
Decrypts using a brute force method.
'''

def encrypt_caesar_cipher(message, shift):
    '''This function takes a message and outputs a caesar cipher encryption based on a chosen shift.
    Parameters: The message being encrypted (message); the shift that the user wants (shift)--25 possible
    Note: Only 25 shifts are possible because a shift of 0 or 26 will result in the same message.
    Returns: the new caesar cipher encrypted message
    '''
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryption = ""
    for character in message:  # For each character in the message...
        if character == " ":
            encryption += " "  # Keep spaces as they are
        elif character in ALPHABET:  # If the character is in the alphabet...
            num = ALPHABET.find(character)
            num = (num + shift) % 26
            encryption += ALPHABET[num]
        else:
            encryption += character
    return encryption

def encrypt_file(input_file_path, shift, output_file_path): # A useful function for future refactoring!
    '''This function reads a plaintext file, encrypts its content using the Caesar cipher, and writes the encrypted text to a new file.'''
    with open(input_file_path, 'r') as file:
        plaintext = file.read()
    
    encrypted_text = encrypt_caesar_cipher(plaintext.upper(), shift)

    with open(output_file_path, 'w') as file:
        file.write(encrypted_text)

    print(f"Encrypted text written to {output_file_path}")
    
def decrypt_caesar_cipher(encrypted_message):
    '''This function takes an encrypted message and runs it through all 26 possible caesar cipher shifts.
    Parameters: The encrypted message (encrypted_message)
    Returns: All possible decrypted messages based on the 26 shifts. The correct decryption should be a legible message.
    '''
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for shift in range(len(ALPHABET)): #For each possible shift...
        decryption = ""
        for character in encrypted_message: #For each character in the message...
            if character == " ": # if the character is a space...
                decryption += " "  # Keep spaces as they are
            elif character in ALPHABET: #If the character is in the alphabet...
                num = ALPHABET.find(character) #Find the index of the character in the alphabet
                num = (num - shift) % 26
                decryption += ALPHABET[num]
            else:
                decryption += character
        print(f"Decryption for Shift = {shift}: {decryption}")

def read_message_from_file(file_path):
    '''This function opens a file to be read.
    Parameters: The file (file_path) 
    Returns: None
    '''
    try:
        with open(file_path, 'r') as file:
            return file.read().strip().upper()
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
        return input("Enter your message:\n>>> ").upper()

def main():
    choice = input("Do you want to (E)ncrypt, (D)ecrypt, or use the Default example? (E/D/Any other key for default):\n>>> ").upper()

#User Input
    if choice in ['E', 'D']:
        message = get_user_input_or_file()
        if message is None:  # Default to example if file not found
            return

#For Encryption
    if choice == 'E':
        while True:
            try:
                shift = int(input("Enter the shift (1-25):\n>>> "))
                if 1 <= shift <= 25:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again.")
        encrypted_message = encrypt_caesar_cipher(message, shift)
        print(f"Encrypted Message: {encrypted_message}")

#For Decryption
    elif choice == 'D':
        decrypt_caesar_cipher(message)

#For Presentation
    else:
        print("Default Example:")
        message = "THIS IS A TEST MESSAGE"
        shift = 3
        encrypted_message = encrypt_caesar_cipher(message, shift)
        print(f"Encrypted Message:  {encrypted_message}")
        decrypt_caesar_cipher(encrypted_message)

if __name__ == "__main__":
    main()
