#coding=utf-8
'''
字典：键值对
'''
student_dict = {'name':'wangwu','age':22,'school':'Beijing'}
print student_dict
student_dict['city'] = 'Tianjin'
print  student_dict

print student_dict['age']
print student_dict.get('name')
print student_dict.get('phone','110')

school_dict = {'name':'Beijing','num':20}
school_dict['teachers'] = 2000
school_dict['num'] = 30
print school_dict.get('name')
print school_dict
del school_dict['teachers']
print school_dict
school_dict.clear()
print school_dict
print("*"*8)
print student_dict
print len(student_dict)
print student_dict.keys()
print student_dict.values()
for k,v in student_dict.items():
    print("key:%s,value:%s"%(k,v))


