#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 __slots__
'''
在 Python 中，__slots__ 是一个用于优化类的特殊属性。
    它可以用来显式地声明类实例中允许存在的属性，从而节省内存并提高访问速度。
    通常，Python 对象通过一个字典来存储其属性，而使用 __slots__ 后，这个字典将被一个固定大小的数组取代，这样可以节省内存。
'''
class Animal:
    __slots__ = ['name', 'species']

    def __init__(self, name, species):
        self.name = name
        self.species = species

# 创建一个 Animal 实例
a = Animal("Lion", "Panthera leo")

# 访问属性
print(a.name)      # 输出: Lion
print(a.species)   # 输出: Panthera leo

# 尝试设置一个未在 __slots__ 中定义的属性会引发 AttributeError
try:
    a.age = 5
except AttributeError as e:
    print(e)  # 输出: 'Animal' object has no attribute 'age'

'''
__slots__ 属性将 Animal 类限制为只有 name 和 species 两个属性。如果你尝试为 Animal 类的实例添加其他属性（如 age），会引发 AttributeError。

使用 __slots__ 的主要优点是节省内存，特别是当需要创建大量的类实例时。
例如，在数据科学或大规模数据处理应用中，使用 __slots__ 可以显著减少内存占用。 
但是需要注意的是，__slots__ 会使类的灵活性降低，因为不能动态添加不在 __slots__ 中定义的属性。
'''

'''
注意事项
    继承：
        如果在父类中使用了 __slots__，在子类中也需要定义 __slots__，否则子类会忽略父类中的 __slots__。
        可以将子类的 __slots__ 定义为父类 __slots__ 的子集或并集。例如：
'''
class Dog(Animal):
    __slots__ = ['breed']

    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

'''
    弱引用：
        如果你需要使用弱引用（如 weakref），需要在 __slots__ 中包含 __weakref__ 属性。
'''