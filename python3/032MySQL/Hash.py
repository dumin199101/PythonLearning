import hashlib
hash = hashlib.md5()
hash.update("Hello world".encode("utf-8"))
print(hash.hexdigest())