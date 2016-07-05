#!/usr/bin/python
# -*- coding: UTF-8 -*-

age = 19
if age >= 18:
    print 'adult'
else:
    print 'teenager'
    
age = 10
if age>=18:
    print 'adult'
elif age>8:
    print 'teenager'
elif age>3:
    print 'kid'
else:
    print 'baby'
    
names = ['Ala', 'Clock', 'Momo', 'Bobo']
for name in names:
    print name

x = 0
N = 3
while x < N:
    print x
    x = x + 1

x = 1
s = 0
while True:
    s = s + x
    x = x + 1
    if x > 5:
        break
print s

L = [22, 33, 44, 55]
s = 0
for n in L:
    if n < 40:
        continue
    s = s + n
print s

names = ['Alin', 'Coco', 'Momo', 'Bobo']
#迭代:for循环，迭代取到的是元素本身，而非元素的索引
for name in names:
    print name
#索引迭代：不是真的按索引访问，而是由enumerate函数自动把每个元素变成(index, name)这样的tuple，再迭代
for index, name in enumerate(names):
    print index,name

d = {
     'Adam':88,
     'Lisa':78,
     'Bart':99
     }
#迭代dict的value
for v in d.values(): #values方法：把dict包含的value转换成list
    print v
for v in d.itervalues(): #itervalues方法：不会转换，迭代过程中依次从dict中取出value-比values方法节省空间
    print v

#迭代dict的key和value
for key, value in d.items(): #items方法把dict对象转换成包含tuple的list
    print key, value
for key, value in d.iteritems():
    print key, value
