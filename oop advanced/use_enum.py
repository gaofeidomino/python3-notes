#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用枚举类
'''
当需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：好处是简单，缺点是类型是 int，并且仍然是变量。

更好的方法是为这样的枚举类型定义一个 class 类型，然后，每个常量都是 class 的一个唯一实例。Python 提供了 Enum 类来实现这个功能：
'''
JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

'''
这样就获得了 Month 类型的枚举类，可以直接使用 Month.Jan 来引用一个常量，或者枚举它的所有成员：
'''
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

'''
value 属性则是自动赋给成员的 int 常量，默认从 1 开始计数。
如果需要更精确地控制枚举类型，可以从 Enum 派生出自定义类：
    @unique 装饰器可以帮助检查保证没有重复值
'''
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

'''
访问这些枚举类型可以有若干种方法：
    既可以用成员名称引用枚举常量，又可以直接根据 value 的值获得枚举常量。
'''
day1 = Weekday.Mon
print(day1)
# Weekday.Mon
print(Weekday.Tue)
# Weekday.Tue
print(Weekday['Tue'])
# Weekday.Tue
print(Weekday.Tue.value)
# 2
print(day1 == Weekday.Mon)
# True
print(day1 == Weekday.Tue)
# False
print(Weekday(1))
# Weekday.Mon
print(day1 == Weekday(1))
# True
Weekday(7)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/opt/anaconda3/lib/python3.11/enum.py", line 712, in __call__
#     return cls.__new__(cls, value)
#            ^^^^^^^^^^^^^^^^^^^^^^^
#   File "/opt/anaconda3/lib/python3.11/enum.py", line 1135, in __new__
#     raise ve_exc
# ValueError: 7 is not a valid Weekday
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat