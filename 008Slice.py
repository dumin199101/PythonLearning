#coding=utf-8
#Python的切片功能:
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3] #从索引0开始取，直到索引3为止，但不包括索引3
print L[:3] #如果第一个索引是0，可以省略
print L[-2:-1] #倒着切
L2 = range(100)
print L2[:10] #截取前10个
print L2[-10:]#截取后10个
print L2[:10:2]#截取前10个数，每两个取一个
print L2[:] #取得所有的数
print L2[::5]#所有数，每5个取一个
