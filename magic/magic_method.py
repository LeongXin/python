#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools.command.build_ext import if_dl

__author__ = 'Leong'

#__str__,__repr__
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        #return 'Person(%s, %s)' %(self.name, self.gender)
        return 'Person({0}, {1})'.format(self.name, self.gender)
    #定义__repr__的偷懒方法
    __repr__ = __str__
    
p = Person('pp', 'Male')
print p  #默认调用__str__方法
print p.__repr__()
#python定义了两种方法__str__()和__repr__()；__str__()用于显示给用户,__repr__()用于显示给开发人员

#__cmp__
#对于内置类型，sorted()按照默认的比较函数cmp排序；对于自定义类型，需要自己提供特殊方法__cmp__()
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return 'Student({0}, {1})'.format(self.name, self.score)
    __repr__ = __str__
    def __cmp__(self, st):
        if self.score < st.score:
            return -1
        elif self.score > st.score:
            return 1
        else:
            return 0

L = [Student('kaly', 80), Student('any', 90), Student('sara', 60)]
print sorted(L)
#如果list不仅仅包含Student类，则__cmp__可能会报错

#__len__
#如果一个类表现的像一个list，要获取有多少个元素，就得用len()函数
#要让len()函数工作正常，类必须提供一个特殊方法__len__(),返回元素个数
class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
    
ss = Students('ab', 'sk', 'lv')
print len(ss) #调用__len__方法

#数学运算
#四则运算不局限于int、float,还可以是有理数、矩阵等
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __str__(self):
        return '{0}/{1}'.format(self.p, self.q)    
    __repr__ = __str__
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return float(self.p) / float(self.q)
    
r1 = Rational(1, 3)
r2 = Rational(1, 2)
print r1 + r2  # +:调用__add__方法， print：调用__str__方法

#类型转换
print int(12.34)
print float(12)

#要让int()函数正常工作，需要实现特殊方法__int__()
#要让float()函数正常工作，需要实现特殊方法__float__()
r3 = Rational(6, 4)
print int(r3)
r4 = Rational(8, 4)
print float(r4)

#@property
#直接给属性赋值无法检验值的有效性;setter getter方法调用又不够直接；--用装饰器函数把get/set方法装饰成属性调用
class AStudent(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self): #getter
        return self.__score
    @score.setter
    def score(self, score): #setter
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        else:
            self.__score = score
#第一个score(self)是get方法，用@property装饰，第二个score(self, score)是set方法，用@score.setter装饰；@score.setter是前一个@property装饰后的副产品

ast = AStudent('Bob', 0)
print ast.score #getter

ast.score = 60  #setter
print ast.score

#ast.score = 101

#__slots__:一个类允许的属性列表
#目的：限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用__slots__也能节省内存
class SlotStudent(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score

ss = SlotStudent('slot', 'Male', 80)
ss.name = 'Slot'
ss.score = 90
#ss.grade = 'A'  #AttributeError: 'SlotStudent' object has no attribute 'grade'

#__call__:将一个类实例变成一个可调用对象
#可调用对象，例如：函数（函数其实是一个对象）；f(xxx)--f为可调用对象
class CallPerson(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __call__(self, friend):
        print 'My name is {0}...'.format(self.name)
        print 'My friend is {0}...'.format(friend)

cp = CallPerson('Bobo', 'Male')
cp('Momo') #单看调用无法确认cp是一个函数还是一个类实例
