def Encrypt(message, key):
    message = message.upper().replace(" ", "")
    encrypt = ""
    for i in range(len(message)):
        letter = ord(message[i]) - 65
        s = ord(key[i]) - 65
        letter = (letter + s) % 26 + 65
        encrypt += chr(letter)
    return encrypt

def Decrypt(message, key):
    message = message.upper().replace(" ", "")
    decrypt = ""
    for i in range(len(message)):
        letter = ord(message[i]) - 65
        s = ord(key[i]) - 65
        letter = (letter - s) % 26 + 65
        decrypt += chr(letter)
    return decrypt

message = input("Enter the message: ")
key = input("Enter the key: ")
choice = input("Choose Vernam Cipher Technique (Encrypt/Decrypt): ")

if choice == 'Encrypt':
    encrypted = Encrypt(message, key)
    print(f"Encrypted Text: {encrypted}")
elif choice == 'Decrypt':
    decrypted = Decrypt(message, key)
    print(f"Decrypted Text: {decrypted}")
else:
    print("Invalid Choice.")
