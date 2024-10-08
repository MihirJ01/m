def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encryption(string, key):
    encrypt_text = [(ord(string[i]) + ord(key[i])) % 26 + ord('A') for i in range(len(string))]
    return "".join(map(chr, encrypt_text))

def decryption(encrypt_text, key):
    orig_text = [(ord(encrypt_text[i]) - ord(key[i]) + 26) % 26 + ord('A') for i in range(len(encrypt_text))]
    return "".join(map(chr, orig_text))

if __name__ == "__main__":
    string = input("Enter the message: ").upper()
    keyword = input("Enter the keyword: ").upper()
    key = generateKey(string, keyword)
    encrypt_text = encryption(string, key)
    print(f"Encrypted message: {encrypt_text}")
    print(f"Decrypted message: {decryption(encrypt_text, key)}")
