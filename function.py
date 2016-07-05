#!/usr/bin/python
# -*- coding: UTF-8 -*-

print abs(-20)
print cmp(1, 2)
print int('123')
print str(123)

def square_of_sum(l):
    s = 0
    for x in l:
        s = s + x * x
    return s

print square_of_sum([1, 2 ,3])   

#函数返回多值：返回值看做一组tuple
import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print x, y

r = move(100, 100, 60, math.pi/6) 
print r

#递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

r = fact(3)
print r

#定义默认参数：默认参数只能定义在必需参数后面
def power(x, n = 2):
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s

r = power(2, 3)
print r

r = power(2)
print r

#定义可变参数：args看做一组tuple
def happy(*args):
    print args, "is", "happy"
happy()
happy("Tom")
happy("Tom", "Coco")

#生成列表
print range(1, 11)
print [x * x for x in range(1, 11)]  #列表生成式
print [x * x for x in range(1, 11) if x % 2 == 0]  #条件过滤

d = {
     'Adam':88,
     'Lisa':78,
     'Bart':99
     }
tds = ['<tr><td>%s</td><td>%s</td></tr>' %(name, score) for name, score in d.iteritems()] #%s：字符替换，字符串通过%进行格式化
print '<table>'
print '<tr><th>Name</th><th>Score</th></tr>'
print '\n'.join(tds)  #join方法可以将list拼接成一个字符串:按照指定的拼接符拼接列表内所有元素
print '</table>'

print [m + n for m in 'ABC' for n in '123']  #多层表达式
