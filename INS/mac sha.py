import hashlib

str_val = input("Enter the value to encode: ")
result = hashlib.sha1(str_val.encode())
print(f"The hexadecimal equivalent of SHA1 is: {result.hexdigest()}")
