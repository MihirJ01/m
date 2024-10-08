def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha(): 
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    
    return result

text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher(text, shift)
print(f"Encrypted text: {encrypted}")

decrypted = caesar_cipher(encrypted, -shift)
print(f"Decrypted text: {decrypted}")
