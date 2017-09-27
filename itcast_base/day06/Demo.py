#coding=utf-8
#传递可变变量，+=跟+的区别：+=直接在原变量修改，+在新变量修改,与原来没有关系
def test(list):
    list +=list
    print "================="
    print id(list)
    print list

list = [11,22,33]
test(list)
print "+++++++++++++"
print id(list)
print list

print "********************"

def test2(list):
    list = list + list
    print "================="
    print id(list)
    print list

list2 = [33,44,55]
test2(list2)
print "+++++++++++++"
print id(list2)
print list2

#################################
# 24597688
# [11, 22, 33, 11, 22, 33]
# +++++++++++++
# 24597688
# [11, 22, 33, 11, 22, 33]
# ********************
# =================
# 24616912
# [33, 44, 55, 33, 44, 55]
# +++++++++++++
# 24616832
# [33, 44, 55]
