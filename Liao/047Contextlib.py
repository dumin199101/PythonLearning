#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
from contextlib import contextmanager
class Query(object):
    def __init__(self,name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print("Begin")
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

#详解yield：yield相当于reutrn，含有yield的函数是一个Generator，当调用时并没有真正执行，只是返回了一个Gernerator，
#当迭代Generator时才会真正执行函数