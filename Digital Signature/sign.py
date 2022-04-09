import rsa

with open('custom_file.txt', 'rb') as f:
    txt = f.read()

with open('private_key_file.pem', 'rb') as pr:
    private_key = rsa.PrivateKey.load_pkcs1(pr.read())

signature_file = rsa.sign(txt, private_key, 'SHA-256')

print(len(signature_file))

with open('signature_file', 'wb') as sf:
    sf.write(signature_file)