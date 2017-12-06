#_*_coding:utf-8_*_
f = open("demo.py","r",encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line)

print("*"*100)
# print(f.readline())
f.close()
