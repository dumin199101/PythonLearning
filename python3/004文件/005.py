#_*_coding:utf-8_*_
import os
#os.mkdir("test")
# os.rmdir("test")
files = os.listdir(".")
print(files)
print(os.getcwd())
# os.rename("demo.py","demo2.py")
# os.remove("demo1.py")
os.chdir("..")
print(os.getcwd())