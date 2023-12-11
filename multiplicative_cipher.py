
'''
December 11th, 2023
CS5002 Final Project
Multiplicative Cipher encrypter/decrypter
Uses a brute force method of decryption of course.
'''

import math

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
    choice = input("Enter message directly or specify a file? (Type 'M' for message, 'F' for file): \n>>> ").upper()
    if choice == 'F':
        file_path = input("Enter the full path of the .txt file:\n >>> ")
        return read_message_from_file(file_path)
    else:
        return input("Enter your message: \n>>> ")

def multiplicative_inverse(key, modulus):
    '''This function finds the multiplicative inverse of a key modulo a given modulus.
    Parameters: key, modulus
    Returns: The multiplicative inverse of the key modulo the modulus.
    '''
    for i in range(1, modulus):
        if (key * i) % modulus == 1:
            return i
    return None

def multiplicative_encrypt(message, key):
    '''This function encrypts a message using the Multiplicative cipher.
    Parameters: message, key
    Returns: The encrypted message
    '''
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_message = ''
    for char in message.upper():
        if char in ALPHABET:
            char_index = ALPHABET.find(char)
            encrypted_char_index = (char_index * key) % 26
            encrypted_message += ALPHABET[encrypted_char_index]
        else:
            encrypted_message += char  # Non-alphabetic characters unchanged
    return encrypted_message

def multiplicative_decrypt(ciphertext, key):
    '''This function decrypts a ciphertext 
    using the Multiplicative cipher given a key.
    Parameters: ciphertext, key
    Returns: The decrypted message
    '''
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_message = ''
    inverse_key = multiplicative_inverse(key, 26)
    if inverse_key is None:
        raise ValueError("No multiplicative inverse found for the key with respect to modulus 26.")
    for char in ciphertext.upper():
        if char in ALPHABET:
            char_index = ALPHABET.find(char)
            decrypted_char_index = (char_index * inverse_key) % 26
            decrypted_message += ALPHABET[decrypted_char_index]
        else:
            decrypted_message += char  # Non-alphabetic characters unchanged
    return decrypted_message

def brute_force_multiplicative_decrypt(ciphertext):
    '''This function attempts to decrypt a ciphertext using the Multiplicative cipher with all possible coprime keys.
    Parameters: ciphertext
    Returns: The decrypted message
    '''
    for key in range(1, 26):
        if math.gcd(key, 26) == 1:
            decrypted_message = multiplicative_decrypt(ciphertext, key)
            print(f"Attempting key {key}: {decrypted_message}")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): \n >>> ").upper()

    if choice in ['E', 'D']:
        message = get_user_input_or_file()
        if message is None:  # Exit if no message is provided or file is not found
            return

    if choice == 'E':
        while True:
            try:
                key = int(input("Enter the key (must be coprime to 26):\n>>> "))
                if math.gcd(key, 26) == 1:
                    break
                else:
                    print("The key is not coprime to 26. \nCoprime numbers, also known as relatively prime numbers are pairs of numbers that have no common factors other than 1. ") 
                    print ("These are some possible keys: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25.") 
            except ValueError:
                print("Invalid input. Please enter a number.")
        encrypted_message = multiplicative_encrypt(message, key)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        print("Attempting to decrypt through brute force (trying all coprime keys)...")
        brute_force_multiplicative_decrypt(message)

if __name__ == "__main__":
    main()
