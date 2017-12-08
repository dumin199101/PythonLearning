#_*_coding:utf-8_*_
#文件的定位读写
# seek(offset,where)：将文件指针定位的指定的偏移处：where:0:开头 1:指针所在位置 2:末尾
# tell():报告文件指针的位置
f = open("009给Python程序传递参数.py","r",encoding="utf-8")
f.seek(2,0)
content = f.readline()
print(content)
pos = f.tell()
print(pos)
f.close()


