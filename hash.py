#!python
#!/usr/bin/python
#!/usr/local/bin/python
#!/usr/bin/python -t

import hashlib


def main():
    msg = input("Enter Password: ")
    msg_enc = msg.encode()

    hash_md5 = hashlib.md5(msg_enc)
    hash_sha256 = hashlib.sha256(msg_enc)
    hash_sha512 = hashlib.sha512(msg_enc)

    print("MD5: " + hash_md5.hexdigest())
    print("SHA256: " + hash_sha256.hexdigest())
    print("SHA512: " + hash_sha512.hexdigest())

main()