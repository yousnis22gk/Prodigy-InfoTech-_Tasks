def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  
    return decrypted_text


def caesar_cipher():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (a number): "))
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")


if __name__ == "__main__":
    caesar_cipher()
