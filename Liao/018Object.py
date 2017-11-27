#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
'@property属性进行参数检查'
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError("score must be an integer!")
        if score<0 or score>100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score #注意使用私有属性
s = Student()
s.score = 60   #转化为s.set_score(60)
print(s.score) #转化为s.get_score()
s.score = 9999
print(s.score)

