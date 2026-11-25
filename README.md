# Caesar Cipher

A command-line Python program that encodes and decodes text with a Caesar cipher.

## How it works

Each character is shifted by a fixed number of positions in the ASCII table (0-127), wrapping around at the end of the range. Decoding shifts the characters back by the same amount.

## Usage

Pass the shift value as an argument:

    python3 caesar.py <shift>

Then choose a mode and enter the text:

    Enter 'e' to encode or 'd' to decode: e
    Text to encode: Hello
    Ciphertext: Olssv

To decode, run the program with the same shift, choose `d`, and enter the ciphertext.

## Notes

- Personal learning project from 2023.
- The shift must be an integer. A shift of 0 (or any multiple of 128) leaves the text unchanged, and the program prints a warning.
- Works on ASCII text only. Characters outside the ASCII range are not preserved.
- Because the cipher uses the whole ASCII table, some encoded characters are non-printable and can't be copied as text.
