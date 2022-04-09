import rsa

message = b'this is our text hash'

htext = rsa.compute_hash(message, 'SHA-256')

print(htext.hex())

message = b'this is our text hash'

htext = rsa.compute_hash(message, 'SHA-256')

print(htext.hex())