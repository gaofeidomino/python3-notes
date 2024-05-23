#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取对象信息
'''
拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法
    使用 type()
    使用 isinstance()
    使用 dir()

总是优先使用 isinstance() 判断类型
'''
class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

'''
    type()
        一个变量指向函数或者类，也可以用 type() 判断
        type() 函数返回的是对应的 Class 类型。如果要在 if 语句中判断，就需要比较两个变量的 type 类型是否相同
        判断基本数据类型可以直接写 int，str 等，但如果要判断一个对象是否是函数可以使用 types 模块中定义的常量
'''
type(123)
# <class 'int'>
type('str')
# <class 'str'>
type(None)
# <class 'NoneType'>


type(abs)
# <class 'builtin_function_or_method'>
a = Animal("Lion")
type(a)
# <class '__main__.Animal'>


type(123)==type(456)
# True
type(123)==int
# True
type('abc')==type('123')
# True
type('abc')==str
# True
type('abc')==type(123)
# False


import types
def fn():
    pass

type(fn)==types.FunctionType
# True
type(abs)==types.BuiltinFunctionType
# True
type(lambda x: x)==types.LambdaType
# True
type((x for x in range(10)))==types.GeneratorType
# True


'''
使用 isinstance()
    对于 class 的继承关系来说，使用 type() 很不方便。要判断 class 的类型，可以使用 isinstance() 函数。
    如果继承关系是：object -> Animal -> Dog -> Husky
'''
m = Animal()
d = Dog()
h = Husky()

isinstance(h, Husky)
# True
isinstance(h, Dog)
# True
isinstance(h, Animal)
# True
isinstance(d, Dog) and isinstance(d, Animal)
# True
isinstance(d, Husky)
# False

# 能用 type() 判断的基本类型也可以用 isinstance() 判断
isinstance('a', str)
# True
isinstance(123, int)
# True
isinstance(b'a', bytes)
# True
# 还可以判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))
# True
isinstance((1, 2, 3), (list, tuple))
# True


'''
使用 dir()
    获得一个对象的所有属性和方法，可以使用 dir() 函数，它返回一个包含字符串的 list，比如，获得一个 str 对象的所有属性和方法：
'''
dir('ABC')
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'''
    类似 __xxx__ 的属性和方法在 Python 中都是有特殊用途的，比如 __len__ 方法返回长度。
    在 Python 中，如果调用 len() 函数试图获取一个对象的长度，实际上，在 len() 函数内部，它自动去调用该对象的 __len__() 方法，
    所以，下面的代码是等价的：
'''
len('ABC')
# 3
'ABC'.__len__()
# 3

'''
自己写的类，如果也想用 len(myObj) 的话，就自己写一个 __len__() 方法：
'''
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
len(dog)
# 100

'''配合 getattr()、setattr() 以及 hasattr()，可以直接操作一个对象的状态：'''
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x') # 有属性'x'吗？
# True
obj.x
# 9
hasattr(obj, 'y') # 有属性'y'吗？
# False
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') # 有属性'y'吗？
# True
getattr(obj, 'y') # 获取属性'y'
# 19
obj.y # 获取属性'y'
# 19
getattr(obj, 'z') # 获取属性'z'; 获取不存在的属性，会抛出 AttributeError 的错误
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'

# 可以传入一个 default 参数，如果属性不存在，就返回默认值
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 404

hasattr(obj, 'power') # 有属性 'power' 吗？
# True
getattr(obj, 'power') # 获取属性 'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x102d56ed0>>
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn # fn指向 obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x102d56ed0>>
fn() # 调用 fn() 与调用 obj.power() 是一样的
# 81


'''
只有在不知道对象信息的时候，才会去获取对象信息。如果可以直接写：
'''
sum = obj.x + obj.y
'''
就不要写：
'''
sum = getattr(obj, 'x') + getattr(obj, 'y')

# 正确的用法的例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

def readData(fp):
    print(fp)
    pass