#coding:utf-8
import functools
#高阶函数:既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(a,b,f):
    return f(a)+f(b)
print add(-1,2,abs)
#类比PHP的array_map跟array_walk
#map函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
L = [1,2,3,4,5]
def f(x):
    return x*x
print map(f,L) #[1, 4, 9, 16, 25]
#reduce函数：这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def mul(a,b):
    return a-b
print reduce(mul,L) #120
print "------------------"
#filter函数，类比PHP的array_filter,filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
#移除字符串头部跟尾部的空白字符
def not_empty(s):
    return s and s.strip()
print filter(not_empty,['a','',0,False,'123'])
#sorted排序函数
print sorted([36, 5, 12, 9, 21])
def reverse_cmp(x,y):
    if x>y:
        return -1
    elif x<y:
        return 1
    else:
        return 0
#自定义逆序排列
print sorted([36, 5, 12, 9, 21],reverse_cmp)
#按照字母排序:默认是按照ASCII进行排序
print sorted(['bob', 'about', 'Zoo', 'Credit'])
def cmp_ignore_case(s1, s2):
    s1 = s1.upper()
    s2 = s2.upper()
    if s1<s2:
        return -1
    elif s1>s2:
        return 1
    else:
        return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)
#返回函数
def lazy_sum(*args):
    def sum():
        res = 0
        for i in args:
            res = res + i
        return res
    return sum

f = lazy_sum(1,3,5,7,9)
print f #<function sum at 0x016B5DF0>
print f()
#每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print f1 == f2 #False
#匿名函数：使用lambda表达式来声明匿名函数
print map(lambda x:x*x,[1,3,4,5,6])

#函数也可以看做是对象
def now():
    print '2017-05-12'
f = now
print now.__name__
print f.__name__
#我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#实质：decorator就是一个返回函数的高阶函数

def log(func):
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return wrapper

now = log(now)
now()

#偏函数
#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int,base = 2)
print int2('100')

















