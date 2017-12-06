#注意模式选择：r+:覆盖写 w+:清空写 a+:追加写
f = open("001.py","r",encoding='utf-8')
f1 = open("demo1.py","w+",encoding="utf-8")
while True:
    content = f.read(50)
    if len(content)==0:
        break
    f1.write(content)
f.close()
f1.close()
print("Copy is finished!!!")