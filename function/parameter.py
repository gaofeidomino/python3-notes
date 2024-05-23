#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数
# 空函数
def nop():
    pass

# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
age = 0
if age >= 18:
    pass

# 函数参数

# 参数检查
# 数据类型检查可以用内置函数 isinstance() 实现
def my_abs(x):
    if not isinstance(x, (int, float)):     # 只允许整数和浮点数类型的参数
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 位置参数
def power_one(x):
    return x * x

power_one(5)


# 默认参数
# # 设置默认参数时，有几点要注意：
# # # 一是必选参数在前，默认参数在后，否则Python的解释器会报错；
# # # 二是当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
def power_two(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * n
    return s

power_two(5)
power_two(5, 3)

def enroll(name, gender, age=6, city='Beijing'):
    print(name, gender, age, city)

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
# # # city参数用传进去的值，其他默认参数继续使用默认值
enroll('Adam', 'M', city='Tianjin')

def add_end_error(L=[]):
    L.append('END')
    return L
# # # ⚠️⚠️⚠️
# # # 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end_proper(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数
# # 可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]

calc(nums[0], nums[1], nums[2])
calc(*nums)


# 关键字参数
# # 允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person_one(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print(name, age, kw)

person_one('Bob', 15, city='Beijing')

extra = { 'city': 'LanZhou', 'gender': 'male' }

person_one('Jack', 24, city=extra['city'], job=extra['job'])
person_one('Bob', 15, **extra)

# # 命名关键字参数
# # # 要限制关键字参数的名字，可以用命名关键字参数
# # # 特殊分隔符 * 后面的参数被视为命名关键字参数

# # # # 只接收city和job作为关键字参数
def person_two(name, age, *, city, job):
    print(name, age, city, job)

person_two('Jack', 24, city='Beijing', job='Engineer') 
# Jack 24 Beijing Engineer

# # # 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 *
def person_three(name, age, *args, city, job):
    print(name, age, args, city, job)

# # # # 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
person_three('Jack', 24, 'Beijing', 'Engineer')
# # # # TypeError: person_three() missing 2 required keyword-only arguments: 'city' and 'job'

def person_four(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person_four('Jack', 24, job='Engineer')

# # # # ⚠️⚠️⚠️⚠️⚠️⚠️
# # # # 特别注意，如果没有可变参数，就必须加一个 * 作为特殊分隔符。如果缺少 * ，Python解释器将无法识别位置参数和命名关键字参数
def person_five(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


# 参数组合
# # 必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数可以组合使用
# # 但是请注意，⚠️⚠️，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f_one(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f_two(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f_one(1, 2)
f_one(1, 2, c=3)
f_one(1, 2, 3, 'a', 'b')
f_one(1, 2, 3, 'a', 'b', x=99)

# a = 1 b = 2 c = 0 args = () kw = {}
# a = 1 b = 2 c = 3 args = () kw = {}
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

f_two(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# # 通过一个tuple和dict，调用上述函数
args1 = (1, 2, 3, 4)
kw1 = {'d': 99, 'x': '#'}

f_one(*args1, **kw1)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args2 = (1, 2, 3)
kw2 = {'d': 88, 'x': '#'}

f_two(*args2, **kw2)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}



# 小结
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。