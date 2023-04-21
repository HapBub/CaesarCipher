import sys

# Getting letters

letters = 'abcdefghijklmnopqrstuvwxyz'

# Defining the function that will convert our text into cipher

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()

        # In case the written character is 'Space' (optional, easier to read thus easier to guess)

        if letter == ' ':
            ciphertext += letter

        # For other special characters:

        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter

            # Finally, making sure the letters respawn as 'newindex' reaches the end of the line:

            else:
                newindex = index + key
                if newindex >= 26:
                    newindex -= 26
                ciphertext += letters[newindex]
    return ciphertext

# Defining the function that will convert our cipher into text

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter == ' ':
            plaintext += letter
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                newindex = index - key
                if newindex < 0:
                    newindex += 26
                plaintext += letters[newindex]
    return plaintext

# Making the program interact with the user

print()
print("choose 'e' for encryption or 'd' for decryption")
userinput = input('e/d: ').lower()
print()
    
if userinput == 'e':

    # When executing the program, you'll have to specify an integer argument from 1-26

    key = int(sys.argv[1])
    text = input('enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'ciphertext: {ciphertext}')

elif userinput == 'd':
    key = int(sys.argv[1])
    text = input('enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'plaintext: {plaintext}')



    
