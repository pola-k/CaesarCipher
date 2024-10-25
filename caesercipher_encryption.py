import random

READFILE = open("input.txt" , 'r')
key = random.randint(1,25)

encrypted_data = ""

for line in READFILE:
    data = line.strip("\n")
    for char in data:
        if char.islower():
            char = chr((ord(char) + key - 97) % 26 + 97)
        elif char.isupper():
            char = chr((ord(char) + key - 65) % 26 + 65)
        encrypted_data += char
    encrypted_data += '\n'

READFILE.close()

WRITEFILE = open("encrypted_text.txt" , "w")
WRITEFILE.write(encrypted_data)
WRITEFILE.close()