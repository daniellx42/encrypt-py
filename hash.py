#!python
#!/usr/bin/python
#!/usr/local/bin/python
#!/usr/bin/python -t

import hashlib

x = hashlib.md5("tuturu")
x.update("tuturu")
print "MD5: " + x.hexdigest()

y = hashlib.sha256()
y.update("tuturu")
print "SHA256: " + y.hexdigest()

z = hashlib.sha512()
z.update("tuturu")
print "SHA512: " + z.hexdigest()
