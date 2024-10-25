Here's a revised README file tailored to your GitHub repository:

---

# Caesar Cipher Encryption and Brute-Force Decryption

## Overview

This project implements a simple encryption mechanism using the **Caesar Cipher** algorithm, along with a brute-force decryption method. The goal is to encrypt plaintext and allow users to decrypt the ciphertext without prior knowledge of the key used during encryption.

## Features

- **Encryption**: Encrypts plaintext using the Caesar Cipher method with a randomly selected key.
- **Brute-Force Decryption**: Attempts to decrypt the ciphertext by testing all possible keys and checks for valid English text.
- **Output Files**: Each decrypted attempt is saved to a separate text file for easy review.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - `langdetect` for language detection (install using `pip install langdetect`)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/pola-k/CaesarCipher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CaesarCipher
   ```

### Usage

#### Encrypting Text

1. Prepare your `input.txt` file containing the plaintext you want to encrypt.
2. Run the encryption script:
   ```bash
   python caesercipher_encryption.py
   ```
3. The encrypted text will be saved in `encrypted_text.txt`.

#### Brute-Force Decryption

1. Run the brute-force decryption script:
   ```bash
   python caesercipher_bruteforce.py
   ```
2. Each decrypted attempt will be saved in separate files named `decrypted_text_key_X.txt`, where `X` is the key used for decryption.

### Example

Here’s how you can use the scripts:

- Create a text file `input.txt`:
  ```
  Hello, World!
  This is a test message for encryption.
  ```
- Run the encryption script to generate `encrypted_text.txt`.
- Then run the decryption script to produce decrypted files.

### Code Explanation

- **caesercipher_encryption.py**: Contains functions to read plaintext, encrypt it using the Caesar Cipher, and save the output.
- **caesercipher_bruteforce.py**: Contains the brute-force decryption logic that checks each possible key, saves valid outputs, and uses language detection to identify plausible English text.
