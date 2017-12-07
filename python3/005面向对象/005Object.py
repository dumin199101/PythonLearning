#_*_coding:utf-8_*_
#工厂方法模式：
#基类
class Store(object):
    #选择车
    def select_car(self,car_type):
        pass
    #下订单：
    def order(self,car_type):
        return self.select_car(car_type)
#具体实现
class BMWStore(Store):
    #重写选车方法：
    def select_car(self,car_type):
        return BMWFactory.select_car_by_type(car_type)
#造车工厂
class BMWFactory(object):
    def select_car_by_type(self,car_type):
        pass

bmw = BMWStore()
bmw.order('720Li')