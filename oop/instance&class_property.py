#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 实例属性和类属性
'''
由于 Python 是动态语言，根据类创建的实例可以任意绑定属性。
给实例绑定属性的方法是通过实例变量，或者通过 self 变量：
    如果 Student 类本身需要绑定一个属性可以直接在 class 中定义属性，这种属性是类属性，归 Student 类所有：
        定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到

    在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
    因为相同名称的实例属性将屏蔽掉类属性，但是当删除实例属性后，再使用相同的名称，访问到的将是类属性。


实例属性属于各个实例所有，互不干扰；
类属性属于类所有，所有实例共享一个属性；
不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''
class Student(object):
    name = 'Student'

    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

s = Student() # 创建实例 s
print(s.name) # 打印 name 属性，因为实例并没有 name 属性，所以会继续查找 class 的 name 属性
# Student
print(Student.name) # 打印类的 name 属性
# Student
s.name = 'Michael' # 给实例绑定 name 属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的 name 属性
# Michael
print(Student.name) # 但是类属性并未消失，用 Student.name 仍然可以访问
# Student
del s.name # 如果删除实例的 name 属性
print(s.name) # 再次调用 s.name，由于实例的 name 属性没有找到，类的 name 属性就显示出来了
# Student