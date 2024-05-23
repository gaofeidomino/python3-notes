#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承
'''
继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。

回忆一下 Animal 类层次的设计，假设要实现以下 4 种动物：
    Dog - 狗狗；
    Bat - 蝙蝠；
    Parrot - 鹦鹉；
    Ostrich - 鸵鸟。

按照哺乳动物和鸟类归类，可以设计出这样的类的层次：
                       +--> Bat
                       |
          +--> Mammal -+--> Dog
Animal -->|
          +--> Bird -+--> Parrot
                     |
                     +--> Ostrich

如果按照“能跑”和“能飞”来归类，应该设计出这样的类的层次：
                         +--> Ostrich
                         |
          +--> Runnable -+--> Dog
Animal -->|
          +--> Flyable -+--> Parrot
                        |
                        +--> Bat

如果要把上面的两种分类都包含进来，就得设计更多的层次：
    哺乳类：能跑的哺乳类，能飞的哺乳类；
    鸟类：能跑的鸟类，能飞的鸟类。

这么一来，类的层次就复杂了：
                       +--> MRun --> Dog
                       |
          +--> Mammal -+--> MFly --> Bat
Animal -->|
          +--> Bird -+--> BRun --> Ostrich
                     |
                     +--> BFly --> Parrot

如果要再增加“宠物类”和“非宠物类”，这么搞下去，类的数量会呈指数增长，很明显这样设计是不行的。
正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
'''
from socketserver import ForkingMixIn, TCPServer, ThreadingMixIn, UDPServer


class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

'''
现在，要给动物再加上 Runnable 和 Flyable 的功能，只需要先定义好 Runnable 和 Flyable 的类：
'''
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

'''
对于需要 Runnable 功能的动物，就多继承一个 Runnable，例如 Dog：
对于需要 Flyable 功能的动物，就多继承一个 Flyable，例如 Bat：
通过多重继承，一个子类就可以同时获得多个父类的所有功能。
'''
class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass


'''MixIn'''
'''
在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich 继承自 Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable。
这种设计通常称之为 MixIn。

为了更好地看出继承关系，把 Runnable 和 Flyable 改为 RunnableMixIn 和 FlyableMixIn。
类似的，还可以定义出肉食动物 CarnivorousMixIn 和植食动物 HerbivoresMixIn，让某个动物同时拥有好几个 MixIn：
'''
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn): # type: ignore
    pass

'''
MixIn 的目的就是给一个类增加多个功能，这样，在设计类的时候，优先考虑通过多重继承来组合多个 MixIn 的功能，而不是设计多层次的复杂的继承关系。

Python 自带的很多库也使用了 MixIn。
    举个例子，Python 自带了 TCPServer 和 UDPServer 这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，
    这两种模型由 ForkingMixIn 和 ThreadingMixIn 提供。通过组合，就可以创造出合适的服务来。
    
比如，编写一个多进程模式的 TCP 服务，定义如下：
'''
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

'''
编写一个多线程模式的UDP服务，定义如下：
'''
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

'''
如果打算搞一个更先进的协程模型，可以编写一个 CoroutineMixIn：
'''
class MyTCPServer(TCPServer, CoroutineMixIn): # type: ignore
    pass



'''多重继承的示例'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Canine(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says Woof!"

class Feline(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Canine):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Feline):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

class Hybrid(Canine, Feline):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} can bark and meow!"

# 示例
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", "Tabby")
hybrid = Hybrid("Mystery")

print(dog.speak())   # 输出: Rex says Woof!
print(cat.speak())   # 输出: Whiskers says Meow!
print(hybrid.speak())  # 输出: Mystery can bark and meow!

'''
在这个示例中，Hybrid 类继承了 Canine 和 Feline 两个基类，并覆盖了 speak 方法。
'''

'''
构造函数调用顺序：
    多重继承时，需要确保正确调用所有基类的构造函数。可以使用 super() 来自动解决顺序问题。
    Python 使用 C3 线性化算法（即方法解析顺序 MRO）来决定方法和属性的搜索顺序。
'''
'''
MRO（方法解析顺序）：
    Python 中，可以使用 ClassName.mro() 方法来查看类的解析顺序。例如：
'''
print(Hybrid.mro())
'''
    这将输出 [<class '__main__.Hybrid'>, <class '__main__.Canine'>, <class '__main__.Feline'>, <class '__main__.Animal'>, <class 'object'>]，表示 Hybrid 类的 MRO。
'''
'''
避免钻石继承问题：
    如果一个类通过多条继承路径继承自同一个基类，就可能遇到钻石继承问题。Python 使用 MRO 来解决这个问题，确保每个基类只被调用一次。
'''
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
    def method(self):
        print("D method")
        super().method()

d = D()
d.method()

# D method
# B method
# C method
# A method