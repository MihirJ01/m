def encrypt(layers, plain_text):
    plain_text = plain_text.replace(" ", "").upper()
    rail = [""] * layers
    layer = 0
    for character in plain_text:
        rail[layer] += character
        if layer >= layers - 1:
            layer = 0
        else:
            layer += 1
    return "".join(rail)

def main():
    layers = int(input("Enter the number of layers: "))
    plain_text = input("Enter the plain text: ")
    cipher_text = encrypt(layers, plain_text)
    print(f"Encrypted text: {cipher_text}")

if __name__ == '__main__':
    main()
