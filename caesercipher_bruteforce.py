import string
from langdetect import detect

def decrypt_caesar_cipher(encrypted_text, key):
    decrypted_data = ""
    for char in encrypted_text:
        if char.islower():
            char = chr((ord(char) - key - 97) % 26 + 97)
        elif char.isupper():
            char = chr((ord(char) - key - 65) % 26 + 65)
        decrypted_data += char
    return decrypted_data

READFILE = open("encrypted_text.txt" , "r")
encrypted_data = READFILE.read()
READFILE.close()

for key in range(1, 26):
    decrypted_text = decrypt_caesar_cipher(encrypted_data, key)
    try:
        if detect(decrypted_text) == 'en':
            filename = f"decrypted_text_key_{key}.txt"
            WRITEFILE = open(filename, "w")
            WRITEFILE.write(decrypted_text)
            WRITEFILE.close()
            print(f"Decrypted text saved to {filename}")
            print(f"Possible English text found with key = {key}")
    except:
        continue