import rsa

pub_key, pri_key = rsa.newkeys(1024)

def load_keys(filename):
    with open(filename, 'wb') as f:
        if filename == 'pub_key_file.pem':
            f.write(pub_key.save_pkcs1('PEM'))
        elif filename == 'pri_key_file.pem':
            f.write(pri_key.save_pkcs1('PEM'))

load_keys('pub_key_file.pem')
load_keys('pri_key_file.pem')