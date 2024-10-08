import numpy as np
def generate_key_matrix(key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    matrix = []
    used_chars = set()
    for char in key:
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)


    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)

    return np.array(matrix).reshape(5, 5)


def find_position(matrix, letter):
    result = np.where(matrix == letter)
    return result[0][0], result[1][0]  


def prepare_text(text):
    prepared_text = []
    text = text.replace("j", "i")  
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1] if (i + 1 < len(text)) else 'x'

        if char1 == char2:
            prepared_text.append(char1 + 'x')
            i += 1
        else:
            prepared_text.append(char1 + char2)
            i += 2

    if len(prepared_text[-1]) == 1:  
        prepared_text[-1] += 'x'

    return prepared_text


def encrypt_digraph(digraph, matrix):
    char1, char2 = digraph
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    
    if row1 == row2:
        
        encrypted_pair = matrix[row1, (col1 + 1) % 5] + matrix[row2, (col2 + 1) % 5]
    elif col1 == col2:
        
        encrypted_pair = matrix[(row1 + 1) % 5, col1] + matrix[(row2 + 1) % 5, col2]
    else:
        
        encrypted_pair = matrix[row1, col2] + matrix[row2, col1]

    return encrypted_pair


def decrypt_digraph(digraph, matrix):
    char1, char2 = digraph
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    
    if row1 == row2:
        
        decrypted_pair = matrix[row1, (col1 - 1) % 5] + matrix[row2, (col2 - 1) % 5]
    elif col1 == col2:
        
        decrypted_pair = matrix[(row1 - 1) % 5, col1] + matrix[(row2 - 1) % 5, col2]
    else:
        
        decrypted_pair = matrix[row1, col2] + matrix[row2, col1]

    return decrypted_pair


def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = text.replace(" ", "").lower()  
    prepared_text = prepare_text(text)

    encrypted_text = ""
    for digraph in prepared_text:
        encrypted_text += encrypt_digraph(digraph, matrix)

    return encrypted_text


def playfair_decrypt(text, key):
    matrix = generate_key_matrix(key)
    text = text.replace(" ", "").lower()  
    prepared_text = [text[i:i + 2] for i in range(0, len(text), 2)]

    decrypted_text = ""
    for digraph in prepared_text:
        decrypted_text += decrypt_digraph(digraph, matrix)

    return decrypted_text


key = input("Enter the key: ").lower().replace(" ", "")  
plaintext = input("Enter the text to encrypt: ").lower().replace(" ", "")  

encrypted_text = playfair_encrypt(plaintext, key)
print(f"Encrypted text: {encrypted_text}")


decrypted_text = playfair_decrypt(encrypted_text, key)
print(f"Decrypted text: {decrypted_text}")
