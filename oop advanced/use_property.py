#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 @property
'''在绑定属性时，如果直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：'''
class Student(object):
    pass

s = Student()
s.score = 9999

'''
为了限制 score 的范围，可以通过一个 set_score() 方法来设置成绩，再通过一个 get_score() 来获取成绩，这样，在 set_score() 方法里，就可以检查参数：
'''
class Student(object):
    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

'''
但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
装饰器（decorator）可以给函数动态加上功能。对于类的方法，装饰器一样起作用。Python 内置的 @property 装饰器就是负责把一个方法变成属性调用的：
'''
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

'''
@property 的实现比较复杂，先考察如何使用。把一个 getter 方法变成属性，只需要加上 @property 就可以了，
此时，@property 本身又创建了另一个装饰器 @score.setter，负责把一个 setter 方法变成属性赋值，于是，就拥有一个可控的属性操作：
'''
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
# 60
s.score = 9999
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 10, in score
# ValueError: score must between 0 ~ 100!

'''
注意到 @property，在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过 getter 和 setter 方法来实现的。

还可以定义只读属性，只定义 getter 方法，不定义 setter 方法就是一个只读属性：
'''
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
    
'''
特别注意：属性的方法名不要和实例变量重名。例如，以下的代码是错误的：
class Student(object):

    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth

因为调用 s.birth 时，首先转换为方法调用，在执行 return self.birth 时，又视为访问 self 的属性，于是又转换为方法调用，造成无限递归，最终导致栈溢出报错 RecursionError。
'''

'''
利用 @property 给一个 Screen 对象加上 width 和 height 属性，以及一个只读属性 resolution：
'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height
    

'''示例'''
class Animal:
    def __init__(self, name, species):
        self._name = name  # 使用前缀下划线表示私有属性
        self._species = species

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def species(self):
        """The species property"""
        return self._species

    @species.setter
    def species(self, value):
        if not value:
            raise ValueError("Species cannot be empty")
        self._species = value

# 创建一个 Animal 实例
a = Animal("Lion", "Panthera leo")

# 访问属性
print(a.name)      # 输出: Lion
print(a.species)   # 输出: Panthera leo

# 修改属性
a.name = "Tiger"
a.species = "Panthera tigris"
print(a.name)      # 输出: Tiger
print(a.species)   # 输出: Panthera tigris

# 尝试设置一个无效的值
try:
    a.name = ""
except ValueError as e:
    print(e)  # 输出: Name cannot be empty
