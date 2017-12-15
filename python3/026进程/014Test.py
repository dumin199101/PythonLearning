#coding=utf-8
#利用多进程拷贝文件：
#此处如果加上join方法，那么效果就是先执行完copy任务再打印进度
#此处主进程未结束的原因就是在主进程中循环条件一直未满足，所以一直等待
#注意%号格式及换行输出
import os
from multiprocessing import Pool,Manager

def copy(name,srcFolder,newFolder,q):
    fr = open(srcFolder+"/"+name,"rb")
    fw = open(newFolder+"/"+name,"wb")
    while True:
        content = fr.read(2048)
        fw.write(content)
        if len(content)==0:
            break
    fr.close()
    fw.close()
    #copy完成加入queue
    q.put(name)

def main():
    '''
    多进程copy文件：
    :return:
    '''
    #1.选择要拷贝的文件夹：
    srcFolder = input("请输入要拷贝的文件夹：")
    #2.创建一个同名文件夹+复件
    newFolder = "复件"+srcFolder
    os.mkdir(newFolder)
    #3.获取文件夹中的文件
    files = os.listdir(srcFolder)
    #4.利用多进程进行拷贝
    pool = Pool(6)
    q = Manager().Queue()
    #添加任务：
    for file in files:
        pool.apply_async(copy,args=(file,srcFolder,newFolder,q))
    #pool.close()
    #pool.join()
    #主进程中计算copy进度：
    num = 0
    allNum = len(files)
    while True:
        q.get(True)
        num+=1
        copyRate = num / allNum
        print("\nCopy的进度是：%.2f%%"%(copyRate*100),end="")
        if num==allNum:
            break


if __name__=="__main__":
    main()
