from cryptography.fernet import Fernet
import rsa

key = Fernet.generate_key()
cipher = Fernet(key)

with open('pub_key_file.pem', 'rb') as pk:
    pub_key = rsa.PublicKey.load_pkcs1(pk.read())
    encrypt_symmetric_key = rsa.encrypt(key, pub_key)

with open('custom_file.txt', 'rb') as txt:
    encrypted_file = cipher.encrypt(txt.read())

with open('encrypted_file', 'wb') as ef:
    ef.write(encrypt_symmetric_key)
    ef.write(encrypted_file)