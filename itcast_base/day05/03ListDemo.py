#coding:utf-8
def scanList(name_list):
    for temp in name_list:
        print temp
name_list = ['wangliang','sunjun','zhanghui','qinfeng']
print u"原始数据"
scanList(name_list)
name_list.append('sunwen')
print u"追加数据:append"
scanList(name_list)
print u"追加数据：insert"
name_list.insert(1,"dumin")
scanList(name_list)
age_list = [22,33,44]
print u"追加数据：extend"
name_list.extend(age_list)
print name_list #['wangliang', 'dumin', 'sunjun', 'zhanghui', 'qinfeng', 'sunwen', 22, 33, 44]

name_list[0] = 'haoshuai'
print u"修改第一个元素："
scanList(name_list)

print u"查找元素："
tmp = 'qinfeng'
if tmp in name_list:
    print "In"
else:
    print "not In"
print name_list.index('sunwen',0)
print name_list.count('sunwen')

print u"删除元素"
movie_list = ["速度与激情","变形金刚","霍比特人","战狼"]
del movie_list[0]
print u"通过del方式删除："
for temp in movie_list:
    print temp.decode('utf-8')
print u"通过pop方式删除："
movie_list.pop()
for temp in movie_list:
    print temp.decode('utf-8')
print u"通过remove方式删除："
movie_list.remove('变形金刚')
for temp in movie_list:
    print temp.decode('utf-8')

schoolName = [
    ['北京大学','清华大学'],
    ['天津大学','南开大学'],
    ['重庆大学','西南大学','四川大学']
]

for i,v in enumerate(name_list):
    print i,v

