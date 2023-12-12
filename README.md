# DIY Cryptography
*Roux Institute at Northeastern CS5002 Discrete Structures Fall 2023 Group Final Project*<br>

A collection of programs to encrypt and decrypt messages  using multiple different ciphers. For more information 

## *Features*
* Quick and easy to use.
* Multiple cipher types to encrypt/decrypt messages.
* Options to type message or read in files.

## *Necessary Installations*
The following packages are all required to use all of the programs (requirements differ between programs). Documentation and instructions for installing each package can be found below:<br>

### `Python3`
1. Please ensure that python 3 is installed in your system. Documentation and instructions for installation can be found [here](https://www.python.org/downloads/)

### `rsa`
1. This is a pure Python RSA implementation and is necessary for the `rsa_script.py`.
2. To check if you already have this installed, try entering `pip show rsa` (you may need to use `pip3` if you are a Mac or Homebrew user) in your terminal.
3.Documentation for `rsa` can be found [here](https://pypi.org/project/rsa/). Installation instructions are included.

### `SymPy`
1. This is a Python library for symbolic mathematics. It is necessary for the `hill_cipher.py`.
2. To check if you already have this installed, try entering `pip show sympy` (you may need to use `pip3` if you are a Mac or Homebrew user) in your terminal.
3.Documentation for `sympy` can be found [here](https://docs.sympy.org/latest/index.html). Installation instructions are included.

### `NumPy`
1. This is a Python library for working with large arrays, matrices, and high-level mathematical operations. It is necessary for the `hill_cipher.py` 
2. To check if you already have this installed, try entering `pip show numpy` (you may need to use `pip3` if you are a Mac or Homebrew user) in your terminal.
3. Documentation for `moviePy` can be found [here](https://numpy.org/doc/stable/). Installation instructions are included.

## *Instructions for Use (for each program)*
1. For running `caesar_cipher.py`
    * This program allows the user to encrypt and decrypt messages with caesar cipher. It accepts messages as user input, or reads in from a file.
    * *Encryption*: When prompted, choose the encrypt option (press E) then enter message the desired shift key (0-25).
    * *Decryption*: Choose  option to decrypt (press D) then enter message/file to decrypt. The output will show all possible 25 shifts (a brute force method), with one being the correct legible/decrypted text.
2. For running `baconian_cipher.py`
    * This program allows the user to encrypt and decrypt messages with baconian cipher. It accepts messages as user input, or reads in from a file.
    * *Encryption*: When prompted, choose the encrypt option (press E) then enter message.
    * *Decryption*: Choose  option to decrypt (press D) then enter message/file to decrypt.
3. For running `multiplicative_cipher.py`
    * This program allows the user to encrypt and decrypt messages with multiplicative cipher. It accepts messages as user input.
    * *Encryption*: When prompted, choose the encrypt option (press E) then enter your message. Next,input a co-prime number of 26 to generate the key (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25).
    * *Decryption*: Choose  option to decrypt (press D) then enter message to decrypt. The output will contain  12 possible co-prime key decryptions (a brute force method), with one being the correct legible/decrypted text.
4. For running `hill_cipher.py`
    * Make sure that you have `numpy` and `sympy` installed.
    * This program allows the user to encrypt and decrypt messages with hill cipher using a generated key matrix that must be used for decryption (self-stored on key_matrix.npy). It accepts messages as user input.
    * *Encryption*: When prompted, choose the encrypt option (press E) then enter your message.
    * *Decryption*: Choose  option to decrypt (press D) then enter message to decrypt that has been encrypted by the same program. The same cipher won't do, since you must have the key_matrix used to encrypt.
5. For running `rsa_script.py`
    * Make sure that you have `rsa` installed.
    * This program allows the user to encrypt and decrypt messages with rsa (Rivest-Shamir-Adleman) cipher. It accepts messages as user input. If public/private keys are not available to read, they will be generated (a self-stored `public.pem` and `private.pem`).
    * *Encryption*: When prompted, choose the encrypt option (press E) then enter your message. The encrypted message will be in hex format.
    * *Decryption*: Choose  option to decrypt (press D) then enter message to decrypt.