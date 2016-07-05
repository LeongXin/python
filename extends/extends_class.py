#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Leong'

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
class Student(Person):  #(Person):表明Student类继承自Person类
    def __init__(self, name, gender, score):
        #子类调用父类构造方法初始化父类
        super(Student, self).__init__(name, gender) #函数super(Student, self)返回当前类继承的父类，即Person，然后调用__init__方法
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

p = Person('ming', 'Female')
s = Student('hua', 'Male', 80)
t = Teacher('li', 'Male', 'Chinese')

#isinstance():判断一个变量的类型（内置类型和自定义类型都可以使用）
print isinstance(p, Person)
print isinstance(p, Student)
print isinstance(t, Student)

print isinstance(s, Person)
print isinstance(s, Student)
print isinstance(s, Teacher)

#多态
class APerson(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' %self.name
    
class AStudent(APerson):  #(Person):表明Student类继承自Person类
    def __init__(self, name, gender, score):
        #子类调用父类构造方法初始化父类
        super(AStudent, self).__init__(name, gender) #函数super(Student, self)返回当前类继承的父类，即Person，然后调用__init__方法
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' %self.name

class ATeacher(APerson):
    def __init__(self, name, gender, course):
        super(ATeacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' %self.name

pe = APerson('ming', 'Female')
st = AStudent('hua', 'Male', 80)
te = ATeacher('li', 'Male', 'Chinese')

print pe.whoAmI()
print st.whoAmI()
print te.whoAmI()
#方法调用将作用在实际类型上；
#Python是动态语言，动态语言调用实例方法，不检查类型，只要方法存在，类型正确，就可以调用

#多重继承
class A(object):
    def __init__(self, a):
        print 'init a...'
        self.a = a
    
class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init b...'
        #self.b = b

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init c...'
        #self.c = c
    
class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init d...'
        #self.d = d
        
d = D('a')  #init a 仅执行一次！！！
#多继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用

#获取对象信息
#type()函数获取变量的类型：返回一个Type对象
print type(123) #<type 'int'>
print type(st)  #<class '__main__.AStudent'>

#dir()函数获取变量的所有属性:返回属性的字符串列表
print dir(123)
print dir(st)

#已知一个属性名称，要获取或者设置对象的属性，可以使用getattr()和setattr()
print getattr(st, 'name')

setattr(st, 'name', 'coco')
print st.name

print getattr(st, 'age', 20)  #请求不给默认值时，属性不存在会抛异常；传默认值，属性不存在，返回默认值