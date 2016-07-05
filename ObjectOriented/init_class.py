#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Leong'

#关键字class定义类；
#编程习惯：类名以大写字母开头，紧接着(object)表示类是从哪个类继承下来的
class SimplePerson(object):
    pass

#创建实例
aSan = SimplePerson()
#让每一个实例拥有各自不同的属性：python是动态语言，对每一个实例，都可以直接给他们的属性赋值
#自由的给实例绑定各种属性
aSan.name = 'aSan'
aSan.gender = 'Male'
aSan.birth = '1990-01-02'

aSi = SimplePerson()
aSi.name = 'aSi'
aSi.school = 'ao'
aSi.grade = 2
aSi.grade = aSi.grade + 1

class Person(object):
    #__init__方法的第一个参数必须是self(也可以是别的名字，但是建议习惯用法)，后续参数可以自由指定
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth

#创建实例时，必须提供除self以外的其他参数

gary = Person('gary', 'Male', '1980-09-12')
print gary.birth

###访问限制
#python对属性限制的控制是通过属性名来实现的，如果一个属性有双下划线开头，该属性无法被外部访问
class ControlPerson(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__secret = 'shy'

haha = Person('haha', 'Male', '1980-09-08')
print haha.name

#如果一个属性以'__xxx__'的形式定义，它又可以被外部访问
#以'__xxx__'形式定义的属性在python中被称为特殊属性，通常我们不用来定义普通属性

###实例属性&类属性
class AdrPerson(object):
    address = 'Earth'    #类属性
    def __init__(self, name):
        self.name = name #实例属性

print AdrPerson.address

recal = AdrPerson('Recal')
joey = AdrPerson('Joey')
print recal.address
print joey.address

#由于python是动态语言，类属性也是可以动态添加和修改的
AdrPerson.gender = 'Male'

print AdrPerson.gender
print recal.gender

#通过实例变量修改类属性,会发生什么???
recal.address = 'China'

print AdrPerson.address #Earth
print recal.address     #China
print joey.address      #Earth

#recal.address = 'China'并没有修改类的属性，而是改recal实例绑定了一个新的实例属性address
#访问recal.address时，优先查找实例属性；没有对应的实例属性，查找类属性

#删除冲突的实例属性后，可以获取到类属性
del recal.address
print recal.address     #Earth

#定义实例方法
class MethodPerson(object):
    def __init__(self, name):
        self.name = name
        self.__gender = 'Male'
    #实例方法
    def get_name(self):
        if self.__gender == 'Male':  #实例方法可以访问实例的私有属性
            return self.name + '_M'
        else:
            return self.name + '_F'

cancan = MethodPerson('cancan')
print cancan.get_name()

#类中定义的方法其实也是属性，实际是一个函数对象
print cancan.get_name #返回一个函数对象，绑定到实例的函数

#因为方法也是一个属性，所以，它也可以动态添加到实例上
import types

class DynamicPerson(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    elif self.score >= 60:
        return 'B'
    else:
        return 'C'

man = DynamicPerson('cc', 90)
man.get_grade = types.MethodType(fn_get_grade, man, DynamicPerson) #用types.MethodType()把一个函数变为一个方法

print man.get_grade()

#类方法
class ClassPerson(object):
    count = 0
    
    @classmethod   #通过标识@classmethod,将方法绑定到ClassPerson类上；方法的第一个参数是类本身，起名为cls
    def how_many(cls):
        return cls.count
    
    def __init__(self, name):
        self.name = name
        ClassPerson.count = ClassPerson.count + 1

print ClassPerson.how_many()

classman = ClassPerson('mm')
print ClassPerson.how_many()
