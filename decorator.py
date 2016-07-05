#!/usr/bin/python
# -*- coding: UTF-8 -*-
import functools

###装饰器###

#不带参数的装饰器
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()..'  #注意：双下划线
        return f(x)
    return fn

@log
def f1(x):
    return x * 2

print f1(2)

#保证任意个数的参数总能正常调用
def new_log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()..'
        return f(*args, **kw)
    return fn

@new_log
def f2(x, y):
    return x + y

print f2(1,2)

#带参数的装饰器 
def info_log(prefix):
    def log_decorator(f):
        def fn(*args, **kw):
            print '[%s] %s...' %(prefix, f.__name__)
            return f(*args, **kw)
        return fn
    return log_decorator

@info_log('DEBUG')
def f3(x, y):
    return x - y

@info_log('INFO')
def f4(x, y):
    return x * y

print f3(3,2)
print f4(3,2)

# @改变函数属性__name__,__doc__
def f5(x):
    pass
print f5.__name__  #f5

@new_log
def f6(x):
    pass
print f6.__name__  #fn,而不是f6

#python内置的functools可以自动完成函数属性复制的任务
def copy_log(f):
    @functools.wraps(f)  #f的函数属性拷贝到fn函数
    def fn(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return fn;

@copy_log
def f7(x):
    pass
print f7.__name__ #f7
#由于函数签名修改为(*args, **kw)，所以，无法获得原函数的参数信息。即便采用固定参数(x)来装饰，也可能改变原函数的参数名

#偏函数
print int('10')    #默认十进制转换字符串
print int('10', 2) #显示申明二进制转换字符串

#简化二进制转换调用
def int2(x, base=2):
    return int(x, base)

print int2('10')

#functools.partial:帮助我们创建一个偏函数，不需要自己定义int2;可以把一个参数多的函数编程一个参数少的函数
new_int2 = functools.partial(int, base=2)  
print new_int2('11')