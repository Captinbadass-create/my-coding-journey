"""
Caesar Cipher CLI Tool

An interactive command-line application that allows users to encrypt,
decrypt, perform brute-force analysis, and process files using the Caesar cipher.
"""

import random
import string


def caesar(text: str, shift: int, encrypt: bool = True) -> str:
    """
    Encrypts or decrypts text using the Caesar cipher algorithm.

    Parameters:
        text (str): The input string to transform.
        shift (int): The shift key amount (must be between 1 and 25).
        encrypt (bool): True to encrypt, False to decrypt. Defaults to True.

    Returns:
        str: The transformed text with case preserved and non-alphabet characters untouched.
    """
    # Validate that the shift parameter is an integer
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer value.")

    # Enforce shift boundary conditions
    if not (1 <= shift <= 25):
        raise ValueError("Shift must be an integer between 1 and 25.")

    # Base alphabet used for character mapping
    alphabet = string.ascii_lowercase

    # Determine direction: positive shift for encryption, negative for decryption
    actual_shift = shift if encrypt else -shift

    # Create the shifted alphabet slice
    shifted_alphabet = alphabet[actual_shift:] + alphabet[:actual_shift]

    # Map original uppercase/lowercase letters to shifted counterparts
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Apply translation map to input text
    return text.translate(translation_table)


def encrypt(text: str, shift: int) -> str:
    """Wrapper function to handle text encryption."""
    return caesar(text, shift, encrypt=True)


def decrypt(text: str, shift: int) -> str:
    """Wrapper function to handle text decryption."""
    return caesar(text, shift, encrypt=False)


def generate_random_key() -> int:
    """Generates a random integer shift key between 1 and 25."""
    return random.randint(1, 25)


def brute_force_decrypt(ciphertext: str) -> None:
    """
    Prints all 25 possible shift variations of ciphertext to break encryption
    without knowing the key beforehand.
    """
    print("\n--- Brute-Force Analysis ---")
    for key in range(1, 26):
        attempt = decrypt(ciphertext, key)
        print(f"Shift {key:2d}: {attempt}")
    print("----------------------------\n")


def process_file(file_path: str, output_path: str, shift: int, mode: str) -> None:
    """
    Reads a source file, applies encryption or decryption, and saves the output.

    Parameters:
        file_path (str): Path to the input file.
        output_path (str): Target path to save the processed file.
        shift (int): The shift key value (1-25).
        mode (str): 'encrypt' or 'decrypt'.
    """
    try:
        # Open and read content from the source file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Transform content based on selected mode
        if mode == "encrypt":
            result = encrypt(content, shift)
        else:
            result = decrypt(content, shift)

        # Write output content to destination file
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(result)

        print(f"\nSuccess! Processed content saved to: {output_path}\n")

    # Handle missing file exceptions gracefully
    except FileNotFoundError:
        print(f"\nError: File '{file_path}' was not found. Check the path and try again.\n")
    except Exception as e:
        print(f"\nAn error occurred while processing the file: {e}\n")


def get_valid_shift() -> int:
    """Prompts the user repeatedly until a valid integer between 1 and 25 is entered."""
    while True:
        try:
            shift = int(input("Enter shift key (1-25): "))
            if 1 <= shift <= 25:
                return shift
            print("Invalid range. Shift must be between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main() -> None:
    """Main execution loop for the interactive terminal application."""
    while True:
        # Terminal interface menu options
        print("=== Caesar Cipher CLI Tool ===")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Encrypt/Decrypt File")
        print("4. Crack Cipher (Brute-Force)")
        print("5. Generate Random Shift Key")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        # Execute selected user action
        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = get_valid_shift()
            print(f"\nEncrypted result: {encrypt(text, shift)}\n")

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = get_valid_shift()
            print(f"\nDecrypted result: {decrypt(text, shift)}\n")

        elif choice == "3":
            mode = input("Enter mode ('encrypt' or 'decrypt'): ").strip().lower()
            if mode not in ["encrypt", "decrypt"]:
                print("\nInvalid mode selected. Please choose 'encrypt' or 'decrypt'.\n")
                continue

            input_file = input("Enter input text file path: ").strip()
            output_file = input("Enter target output file path: ").strip()
            shift = get_valid_shift()
            process_file(input_file, output_file, shift, mode)

        elif choice == "4":
            text = input("Enter ciphertext to analyze: ")
            brute_force_decrypt(text)

        elif choice == "5":
            key = generate_random_key()
            print(f"\nGenerated Random Key: {key}\n")

        elif choice == "6":
            print("Exiting application. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.\n")


# Entry point check
if __name__ == "__main__":
    main()
