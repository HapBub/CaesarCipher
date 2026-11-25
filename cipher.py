import sys

START, SIZE = 32, 95  # printable ASCII: space (32) to ~ (126)


def shift_text(text, shift):
    result = ""
    for char in text:
        code = ord(char)
        if START <= code < START + SIZE:
            code = (code - START + shift) % SIZE + START
        result += chr(code)  # anything else is left unchanged
    return result


def main():
    try:
        shift = int(sys.argv[1])
    except (IndexError, ValueError):
        sys.exit("Usage: python3 caesar.py <integer shift>")

    if shift % SIZE == 0:
        print(f"Warning: a shift divisible by {SIZE} changes nothing!")

    choice = input("Enter 'e' to encode or 'd' to decode: ").lower()
    if choice == "e":
        print("Ciphertext:", shift_text(input("Text to encode: "), shift))
    elif choice == "d":
        print("Plaintext:", shift_text(input("Text to decode: "), -shift))
    else:
        sys.exit("Please choose 'e' for encoding or 'd' for decoding!")


if __name__ == "__main__":
    main()
