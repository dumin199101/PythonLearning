#coding=utf-8
#007模块：一个文件可以看成是一个模块，目录可以看成是一个包，每个包底下有一个__init__.py的文件
#使用模块:
'a test module'
from PIL import Image

__author__='lieyan123091'
import sys

def test():
    args = sys.argv
    if len(args)==1:
        print "Hello World"
    elif len(args)==2:
        print "Hello %s!" % args[1]
    else:
        print "Too Many arguments"
#Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
#引入第三方库
def test2():
    im = Image.open('test.jpg')
    print im.format, im.size, im.mode #JPEG (1920, 3000) RGB
    im.thumbnail((200, 100))
    im.save('thumb.jpg', 'JPEG')

if __name__ == "__main__":
    test()
    test2()


