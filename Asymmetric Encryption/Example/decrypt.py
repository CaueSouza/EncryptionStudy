from cryptography.fernet import Fernet
import rsa

with open('pri_key_file.pem', 'rb') as pkey:
    priv_key = rsa.PrivateKey.load_pkcs1(pkey.read())

with open('encrypted_file', 'rb') as ef:
    efile = ef.read(128)  # 128 bytes = 1024 bits = standard symmetric key size
    efTxt = ef.read()

decrypted_key = rsa.decrypt(efile, priv_key)
cipher = Fernet(decrypted_key)
decrypted_file = cipher.decrypt(efTxt)

with open('decrypted_file.txt', 'wb') as txt:
    txt.write(decrypted_file)
