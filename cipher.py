import sys


shift = int(sys.argv[1])

#Defining the Caesar Cipher encoding program
def Encoder(plaintext, shift):
    if shift % 128 == 0 or shift == 0:
        #Raising an error to avoid a program bug when the end of ascii range is reached
        raise ValueError("Shift value cannot be 0 or divisible by 128!")

    ciphertext = ""

    for char in plaintext:
        charencoded = chr((ord(char) + shift) % 128)
        ciphertext += charencoded

    return ciphertext

#Defining the Caesar Cipher decoding program
def Decoder(ciphertext, shift):
    if shift % 128 == 0 or shift == 0:
        #Same concept here, if the shift is 128*n (where n is an integer) no shift accurs
        raise ValueError("Shift value cannot be 0 or divisible by 128!")

    plaintext = ""

    for char in ciphertext:
        chardecoded = chr((ord(char) - shift) % 128)
        plaintext += chardecoded

    return plaintext


#Choosing to encode or decode
choice = input("Enter 'e' to encode or 'd' to decode: ")

if choice.lower() == 'e':
    plaintext = input("Text to encode: ")

    ciphertext = Encoder(plaintext, shift)
    print("Ciphertext:", ciphertext)

elif choice.lower() == 'd':
    ciphertext = input("Text to decode: ")

    plaintext = Decoder(ciphertext, shift)
    print("Plaintext:", plaintext)

#Raising an error if the specified values are not 'e' or 'd'
else:
    raise ValueError("Please choose 'e' for encoding or 'd' for decoding!")
