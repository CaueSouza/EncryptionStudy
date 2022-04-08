import rsa

paul_pub, paul_pri = rsa.newkeys(1024)

print(paul_pub.save_pkcs1().decode())

e_data = rsa.encrypt(b'this is my secret message', paul_pub)

d_data = rsa.decrypt(e_data, paul_pri)

print(e_data)
print(d_data.decode())