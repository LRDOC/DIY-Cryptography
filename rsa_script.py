'''
December 11th, 2023
CS5002 Final Project
RSA encrypter/decrypter
Decrypts using a private and public key that is saved between sessions.
This allow for the same key to be used for multiple messages.
The keys are generated if they don't exist.
'''

import rsa
import os

# File paths for keys (these will show up in your directory!)
public_key_file = 'public.pem'
private_key_file = 'private.pem'

def save_keys(pub_key, priv_key):
    '''Function to save public and private keys to files.
    Parameters: Public and private keys
    Returns: None
    '''
    with open(public_key_file, 'wb') as p_file: # Write in binary mode (wb = write binary and p_file = public file)
        p_file.write(pub_key.save_pkcs1('PEM'))

    with open(private_key_file, 'wb') as pr_file: # Write in binary mode (pr_file = private file)
        pr_file.write(priv_key.save_pkcs1('PEM')) # Save the private key (Pem = Privacy Enhanced Mail)

def load_keys():
    '''Function to load public and private keys from files.
    Parameters: None
    Returns: Public and private keys
    '''
    with open(public_key_file, 'rb') as p_file: # Read in binary mode
        pub_key = rsa.PublicKey.load_pkcs1(p_file.read()) # Load the public key

    with open(private_key_file, 'rb') as pr_file:
        priv_key = rsa.PrivateKey.load_pkcs1(pr_file.read()) 
    return pub_key, priv_key

def generate_rsa_keys():
    '''Function to generate public and private RSA keys.
    Parameters: None
    Returns: Public and private keys
    '''
    pub_key, priv_key = rsa.newkeys(512)  # Using a larger key size for security and FUN
    save_keys(pub_key, priv_key)
    return pub_key, priv_key

# Check if keys already exist, load them if they do, generate if they don't
if os.path.exists(public_key_file) and os.path.exists(private_key_file):
    public_key, private_key = load_keys()
else:
    public_key, private_key = generate_rsa_keys()

def encrypt_rsa(message, pub_key):
    '''Function for RSA encryption.
    Parameters: Message to be encrypted, public key
    Returns: Encrypted message in hex format
    '''
    encrypted_message = rsa.encrypt(message.encode(), pub_key) # Convert string to binary
    return encrypted_message.hex()  # Convert binary data to hex

def decrypt_rsa(encrypted_message_hex, priv_key):
    '''Function for RSA decryption.
    Parameters: Encrypted message in hex format, private key
    Returns: Decrypted message
    '''
    encrypted_message = bytes.fromhex(encrypted_message_hex)  # Convert hex to binary
    return rsa.decrypt(encrypted_message, priv_key).decode() # Convert binary to string

def read_message_from_file(file_path):
    '''Function to read a message from a file.
    Parameters: File path
    Returns: Message from file
    '''
    try:
        with open(file_path, 'r') as file: # Read in text mode (r = read) and file = file path
            return file.read().strip()
    except FileNotFoundError:
        print("File not found. Try again.")
        return None

def get_user_input_or_file():
    '''Function to get user input or read from file.
    Parameters: None
    Returns: Message/file path
    '''
    choice = input("Enter message directly or specify a file? (Type 'M' for message, 'F' for file):\n>>> ").upper()
    if choice == 'F':
        file_path = input("Enter the full path of the .txt file:\n>>> ")
        return read_message_from_file(file_path)
    else:
        return input("Enter your message:\n>>> ")

def main():
    global public_key, private_key

    choice = input("Do you want to (E)ncrypt, (D)ecrypt, or use the Default example? (E/D/Any other key for default):\n>>> ").upper()

    if choice in ['E', 'D']:
        message = get_user_input_or_file()
        if message is None:
            return

    if choice == 'E':
        encrypted_message_hex = encrypt_rsa(message, public_key)
        print(f"Encrypted Message in hex: {encrypted_message_hex}")

    elif choice == 'D':
        try:
            decrypted_message = decrypt_rsa(message, private_key)
            print(f"Decrypted Message: {decrypted_message}")
        except ValueError:
            print("Invalid input. Please enter the encrypted message in hex format.")

    else:
        message = "THIS IS A TEST MESSAGE"
        print("Default Example: " + message)
        encrypted_message_hex = encrypt_rsa(message, public_key) # Encrypt the message
        print(f"Encrypted Message in hex: {encrypted_message_hex}") # Print the encrypted message in hex
        decrypted_message = decrypt_rsa(encrypted_message_hex, private_key) # Decrypt the message
        print(f"Decrypted Message: {decrypted_message}") # Print the decrypted message

if __name__ == "__main__":
    main()
