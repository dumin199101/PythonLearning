#coding=utf-8
'''
字符串函数测试
'''
str = "i love studying computer science,i love running!"
str1 = "hello \n world"
print str.find('love')
print str.rfind('love')
print str.index('love')
print str.rindex('love')
print str.count('love')
print str.replace('love',u'喜欢')
print str.split(' ')
print str.capitalize()
print str.title()
print str.lower()
print str.upper()
print str.startswith('i')
print str.endswith('!')
print str.ljust(100,'*')
print str.rjust(100,'*')
print str.center(100,'*')
print str.strip()
print str.lstrip()
print str.rstrip()
print str.partition('love')
print str.rpartition('love')
print str1.splitlines()
print str.isalpha()
print str.isdigit()
print str.isalnum()
print str.isspace()
list = ['wang','li','sun']
print ','.join(list)