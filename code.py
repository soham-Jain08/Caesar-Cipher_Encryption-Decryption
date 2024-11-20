def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-letter characters are added unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decrypting is same as encrypting with negative shift

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print("Encrypted Text:", encrypted_text)
    elif choice == 'd':
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")

if _name_ == "_main_":
    main()