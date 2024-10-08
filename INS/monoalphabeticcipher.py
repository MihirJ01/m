import random
alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(original, key=None):
    if key is None:
        l = list(alpha)
        random.shuffle(l)
        key = "".join(l)
    new = [key[alpha.index(letter)] for letter in original]
    return ["".join(new), key]

def decrypt(cipher, key):
    new = [alpha[key.index(letter)] for letter in cipher]
    return "".join(new)

text = input("Enter plain text: ").lower()
e = encrypt(text)
print(f"Encrypted message: {e[0]}\nKey: {e[1]}")
print(f"Decrypted message: {decrypt(e[0], e[1])}")
