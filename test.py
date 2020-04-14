import cryptography
from cryptography.fernet import Fernet

# this file is a test for encrypting keys

my_key = b'oxAH5eINZEzXSNsfP3PpPyi3Jt92-gwVrVfQHaVlvpA='

# encrypt key
def encrypt_key(text):
    f = Fernet(my_key)
    encrypted = f.encrypt(text)
    return encrypted
# decrypt key
def decrypt_key(encrypted):
    f = Fernet(my_key)
    decrypted = f.decrypt(encrypted)
    return decrypted

key = Fernet.generate_key()
print(key)
e = encrypt_key(key)
print(e)
d = decrypt_key(e)
print(d)

assert(d == key)
