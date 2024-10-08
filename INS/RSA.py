import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def coprimes(a):
    return [x for x in range(2, a) if gcd(a, x) == 1 and modinv(x, phi) is not None]

def encrypt(me, e, n):
    return pow(me, e, n)

def decrypt(me, d, n):
    return pow(me, d, n)

p = int(input("Enter value for p: "))
q = int(input("Enter value for q: "))
n = p * q
phi = (p - 1) * (q - 1)
print(f"n = {n}\nEuler's Totient (phi) = {phi}")

print("Co-Primes for given Prime Numbers:", coprimes(phi))
e = int(input("Choose a value for 'e' from Co-Primes: "))
d = modinv(e, phi)
print(f"d = {d}")

message = int(input("Enter the message to be encrypted: "))
encrypted_message = encrypt(message, e, n)
print(f"Encrypted Message: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, d, n)
print(f"Decrypted Message: {decrypted_message}")
