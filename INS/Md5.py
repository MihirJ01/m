import hashlib

result = hashlib.md5(b'CKT')
result1 = hashlib.md5(b'smilely')
print(f"The byte equivalent of hash (CKT) is: {result.digest()}")
print(f"The byte equivalent of hash (smilely) is: {result1.digest()}")
