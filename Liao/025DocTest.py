#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#文档测试案例
def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(5)
    120
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
if __name__=='__main__':
    import doctest
    doctest.testmod()