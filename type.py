#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
print "hello"
print 'hello'

print 'hello','you'

print 200
print 100 + 200 #plus
print '100 + 200 =', 100 + 200 # 中文

print "I'm ok"
print 'say "hello"'
print 'Bob said \"I\'m ok\"'  #转义字符

print r'\(-_-)/\(-_-)/' #raw字符串
print r'''hi, "you".
welcome'''
print r'''hi, "you".
hello,
welcome'''
print r'''hi, "you".
hello,
welcome,
bye'''

print u"中文"
print u'''中文
日文
韩文'''
print ur'''\(-_-)/\(-_-)/
"中文"
"日文"
"韩文"'''

print 10/4   #2
print 10.0/4 #2.5

#and or 短路运算
print True and False
print True or False
print not True

#0、空字符串''、None 看为False
#其他数值、非空字符串看为True
a = True
print a and 'a=T' or 'a=F'

#list 
classmates = ['Michel', 'Bob', 'Tracy']
print classmates
L = ['Momo', 100, True]
print L

print classmates[0]
print classmates[-1]  #倒序索引

classmates.append("Koko") #追加
classmates.insert(0, "coco") #插入
print classmates

print classmates.pop()
print classmates.pop(0)
print classmates

classmates[-1] = "Paul"
print classmates

#tuple 不可修改
t = ('Adam', 'Lisa', 'Bart')
print t

oneT = (1, ) #单元素tuple，与整数１区别开
print oneT

#dict:key-value,无序
d = {
     'Adam':88,
     'Lisa':78,
     'Bart':99
     }
print d
print len(d)
print d['Adam']
if 'Paul' in d:
    print d['Paul']
    
print d.get('Adam')
print d.get('Paul')

d['Paul'] = 72
print d
d['Paul'] = 98
print d

for key in d:
    print key, d.get(key)

#set    
s = set(classmates)
print s
print 'Bob' in s
print 'bob' in s

for name in s:
    print name
    
s.add('Momo')
print s
s.remove('Bob')
print s

#切片Slice-list tuple
classmates = ['Michel', 'Bob', 'Tracy', 'Tony', 'Mary']
print classmates[1:3]  #从索引0开始，直到索引为3为止，但不包括3
print classmates[:3]   #起始索引为0，可以省略
print classmates[:]    #表示从头取到尾
print classmates[::2]  #第三个参数表示每n个元素取一个

#倒序切片：包含起始索引，不包含结束索引
print classmates[-2:]
print classmates[:-2]
print classmates[-4:-1:2]

#对字符串切片
s = 'AB:CD:EF'
print s[:3]

print s.split(':')
print s.split(':').__len__()

