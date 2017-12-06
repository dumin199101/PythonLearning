#_*_coding:utf-8_*_
#复制文件：注意选择字符编码，否则会报错
f = open("demo.py","r",encoding='utf-8')
f1 = open("demo1.py","w",encoding="utf-8")
while True:
    content = f.read(50)
    if len(content)==0:
        break
    f1.write(content)
f.close()
f1.close()
print("Copy is finished!!!")
