#!/usr/bin/python
# -*- coding: UTF-8 -*-

###高阶函数：能接收函数作为参数的函数
def add(x, y, f):
    return f(x) + f(y)

print add(-5,9,abs)

f = abs  #变量可以指向函数
print f(-2)

abs = len #函数名其实就是指向函数的变量
print abs([1,2,3])

###python内置高阶函数

#map:f依次作用于list的每一个元素，得到一个新的list并返回
def f(x):
    return x * x
print map(f, [1,2,3,4,5])

#reduce:函数参数f必须接收两个参数，对list的每个元素反复调用函数f，并返回最终结果集
def f1(x, y):
    return x + y
print reduce(f1, [1,2,3,4,5])
print reduce(f1, [1,2,3,4,5], 100) #reduce可以接受第三个参数，作为计算的初始值

#filter:根据判断结果过滤不符合条件的元素，返回由符合条件的元素组成的新list
def is_odd(x):
    return x%2 == 1
print filter(is_odd, [1,2,3,4,5])

def is_not_empty(s):
    return s and len(s.strip()) > 0  #s.strip(rm):删除s字符串中开头、结尾处的rm序列的字符。当rm为空时，默认删除空白符(包括'\n','\r','\t','')
print filter(is_not_empty, ['tony', '', '  ', None])

#自定义排序函数
print sorted([36,5,12,9,21])  #sorted：默认升序排序

def revert_cmp(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0
print sorted([36,5,12,9,21], revert_cmp)

print sorted(['Zo', 'aoa', 'bob', 'Coco']) #sorted为字符串排序，字符串默认按照ASCLL大小来比较

###返回函数：可以把一些计算延迟执行
def calc_sum(l):
    def lazzy_sum():  #改进：接收函数作为参数-lazzy_sum(f),调用：f(sum)
        return sum(l)
    return lazzy_sum
f = calc_sum([1,2,3])
print f   #lazzy_sum函数
print f() #延迟执行运算

#闭包Closure：内层函数引用了外层函数的变量，然后返回内层函数
#正确使用闭包：确保引用的局部变量在函数返回之后不能变
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1() #9
print f2() #9
print f3() #9
#因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量
    
#匿名函数:lambda x: x * x，关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有一个限制：只能有一个表达式，不能写return语句，返回值就是表达式的结果
#def f(x):
#    return x * x
#print map(f, [1,2,3,4,5])
print map(lambda x: x * x, [1,2,3,4,5])
#返回函数的时候，也可以返回匿名函数
myabs = lambda x: -x if x < 0 else x
print myabs(-1)
print myabs(1)
