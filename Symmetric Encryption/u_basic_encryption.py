from cryptography.fernet import Fernet

with open('mykey.key', 'rb') as k_file:
    key = k_file.read()

print(key)

cipher = Fernet(key)

# Encrypt
with open('custom_file.txt', 'rb') as w_file:
    data = w_file.read()

encrypted_data = cipher.encrypt(data)

with open('encrypted_file', 'wb') as e_file:
    e_file.write(encrypted_data)

# Decrypt
with open('encrypted_file', 'rb') as e_file:
    encrypted_data = e_file.read()

decrypted_data = cipher.decrypt(encrypted_data)

with open('post_encrypted_file.txt', 'wb') as d_file:
    d_file.write(decrypted_data)