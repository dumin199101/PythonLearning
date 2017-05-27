#coding=utf-8
#字符编码：最早的出现的是ASCII码表；二进制存储占用一个字节，可表示0-255（共256个字符），如果要处理中文，那么一个字节就不够了
#这就引入了unicode编码，占用2个字节，最大可表示的数65535，但是如果每个字都用2个字节来存储，又造成了空间的浪费，这时出现了
#utf-8编码，utf-8编码可以根据数字大小不同编为1-6个字节，节省了存储空间。计算机内存中统一使用unicode编码，在文件传输(网页)或者
#保存到硬盘（文件）的时候才会转换为UTF-8编码。
print ord('A')
print chr(65)
#Python的unicode支持
print u'中国'
print u'\u4e2d\u56fd'
#unicode编码跟utf-8编码的转换:1个汉字占3个字节:encode的作用是将unicode编码转换成其他编码的字符串decode的作用是将其他编码的字符串转换成unicode编码
print u'中国'.encode('utf-8')
print '\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8')
print len(u'中国')  #2
print len('ABC')    #3
print len('\xe4\xb8\xad\xe5\x9b\xbd') #6
#格式化字符串输出
# %s字符串  %d:整数 %f:浮点 %02d：整数不够2位，前边补0 %2d:整数不够2位，前边补空格 %.2f:保留小数点后两位
# PHP中可以用%d$来指定第几个参数echo sprintf('My name is %s,My age is %d,I have %2$d brothers','dumin',22);
print "Hello %s,I\'m a Student,My name is %s,My age is %d,My weight is %.2f kg,My ID is %010d" %('Teacher','Dumin',25,55.5,10)


