import rsa

with open('custom_file.txt', 'rb') as f:
    txt = f.read()

with open('public_key_file.pem', 'rb') as puk:
    public_key = rsa.PublicKey.load_pkcs1(puk.read())

with open('signature_file', 'rb') as sf:
    signature_file = sf.read()

verify_file = rsa.verify(txt, signature_file, public_key)

print(verify_file)