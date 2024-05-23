#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器

import time, functools

# 函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2015-3-25')

f = now
f()
# 2015-3-25

# 函数对象有一个 __name__ 属性（注意：是前后各两个下划线），可以拿到函数的名字：
now.__name__
# 'now'
f.__name__
# 'now'

'''
假设要增强 now() 函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改 now() 函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
    本质上，decorator 就是一个返回函数的高阶函数。
'''

# 要定义一个能打印日志的 decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 上面的 log，因为它是一个 decorator，所以接受一个函数作为参数，并返回一个函数。
# 借助 Python 的 @ 语法，把 decorator 置于函数的定义处：
@log
def now():
    print('2015-3-25')

# 调用 now() 函数，不仅会运行 now() 函数本身，还会在运行 now() 函数前打印一行日志：
now()
# call now():
# 2015-3-25

'''
把 @log 放到 now() 函数的定义处，相当于执行了语句： now = log(now)

    由于 log() 是一个 decorator，返回一个函数，所以，原来的 now() 函数仍然存在，只是现在同名的 now 变量指向了新的函数，
    于是调用 now() 将执行新函数，即在 log() 函数中返回的 wrapper() 函数

    wrapper() 函数的参数定义是 (*args, **kw)，因此，wrapper() 函数可以接受任意参数的调用。在 wrapper() 函数内，首先打印日志，再紧接着调用原始函数

如果 decorator 本身需要传入参数，那就需要编写一个返回 decorator 的高阶函数，写出来会更复杂。比如，要自定义 log 的文本：
'''
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 这个 3 层嵌套的 decorator 用法如下：
@log('execute')
def now():
    print('2015-3-25')

now()
# execute now():
# 2015-3-25

'''
和两层嵌套的 decorator 相比，3 层嵌套的效果是这样的： now = log('execute')(now)
    首先执行 log('execute')，返回的是 decorator 函数，再调用返回的函数，参数是 now 函数，返回值最终是 wrapper 函数。
'''

'''
以上两种 decorator 的定义都没有问题，但还差最后一步。
因为函数也是对象，它有 __name__ 等属性，但经过 decorator 装饰之后的函数，它们的 __name__ 已经从原来的 'now' 变成了 'wrapper'：
'''
now.__name__
# 'wrapper'

'''
因为返回的那个 wrapper() 函数名字就是 'wrapper'，所以，需要把原始函数的 __name__ 等属性复制到 wrapper() 函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写 wrapper.__name__ = func.__name__ 这样的代码，Python 内置的 functools.wraps 可以解决，所以，一个完整的 decorator 的写法如下：
'''
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 针对带参数的 decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# import functools 是导入 functools 模块。记住在定义 wrapper() 的前面加上 @functools.wraps(func)


# 设计一个 decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    def wrapper(*args, **kw):
        st = time.time()
        fn(*args, **kw)
        et = time.time()
        print('%s executed in %s ms' % (fn.__name__, st-et))
        return fn(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
# 33
s = slow(11, 22, 33)
# 7986

# fast executed in -0.0009999275207519531 ms
# slow executed in -0.12400031089782715 ms



'''
在面向对象（OOP）的设计模式中，decorator 被称为装饰模式。
OOP 的装饰模式需要通过继承和组合来实现，而 Python 除了能支持 OOP 的 decorator 外，直接从语法层次支持 decorator。
Python 的 decorator 可以用函数实现，也可以用类实现。

decorator 可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
'''

# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print('begin call')
        result = func(*args, **kwargs)
        print('end call')
        return result
    return wrapper

@log_decorator
def my_function():
    print('This is the function')

print(my_function())
# begin call
# This is the function
# end call



'''
写出一个@log的decorator，使它既支持：

@log
def f():
    pass
    
又支持：

@log('execute')
def f():
    pass
'''
def log(arg=None):

    def wrapper(func):
        @functools.wraps(func)

        def inner_wrapper(*args, **kwargs):
            if arg:
                print(arg)

            return func(*args, **kwargs)
        return inner_wrapper

    if callable(arg):
        return wrapper(arg)

    return wrapper