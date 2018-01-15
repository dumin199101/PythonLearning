import hashlib
# md5加密
hash = hashlib.md5()
hash.update("Hello world".encode("utf-8"))
print(hash.hexdigest())

# sha1加密
sha1 = hashlib.sha1()
sha1.update("Hello world".encode("utf-8"))
print(sha1.hexdigest())