#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 继承和多态
'''
在 OOP 程序设计中，当定义一个 class 的时候，可以从某个现有的 class 继承，新的 class 称为子类（Subclass），
而被继承的 class 称为基类、父类或超类（Base class、Super class）。

继承最大的好处是子类获得了父类的全部功能。由于 Animial 实现了 run() 方法，因此，Dog 和 Cat 作为它的子类，自动拥有了 run() 方法。
当然，也可以对子类增加一些方法，比如Dog类：

当子类和父类都存在相同的 run() 方法时，子类的 run() 覆盖了父类的 run()，在代码运行的时候，总是会调用子类的 run()。
这样，就获得了继承的另一个好处：多态。

要理解什么是多态，首先要对数据类型再作一点说明。
当定义一个 class 的时候，实际上就定义了一种数据类型。
定义的数据类型和 Python 自带的数据类型，比如 str、list、dict 没什么两样：
    a = list() # a是list类型
    b = Animal() # b是Animal类型
    c = Dog() # c是Dog类型

判断一个变量是否是某个类型可以用 isinstance() 判断：
    isinstance(a, list)
    # True
    isinstance(b, Animal)
    # True
    isinstance(c, Dog)
    # True
    isinstance(c, Animal)
    # True
    # c 不仅仅是 Dog，c 还是 Animal

因为 Dog 是从 Animal 继承下来的，当创建了一个 Dog 的实例 c 时，c 的数据类型是 Dog，但 c 同时也是 Animal 也没错，Dog 本来就是 Animal 的一种！
所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行。
Dog 可以看成 Animal，但 Animal 不可以看成 Dog。
'''

'''
新增一个 Animal 的子类，不必对 run_twice() 做任何修改，实际上，任何依赖 Animal 作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
多态的好处就是，当需要传入 Dog、Cat、Tortoise…… 时，只需要接收 Animal 类型就可以了，
因为 Dog、Cat、Tortoise…… 都是 Animal 类型，然后，按照 Animal 类型进行操作即可。

由于 Animal 类型有 run() 方法，因此，传入的任意类型，只要是 Animal 类或者子类，就会自动调用实际类型的 run() 方法，这就是多态的意思：
    对于一个变量，只需要知道它是 Animal 类型，无需确切地知道它的子类型，就可以放心地调用 run() 方法，
    而具体调用的 run() 方法是作用在 Animal、Dog、Cat 还是 Tortoise 对象上，由运行时该对象的确切类型决定，

    这就是多态真正的威力：
        调用方只管调用，不管细节，而当新增一种 Animal 的子类时，只要确保 run() 方法编写正确，不用管原来的代码是如何调用的。

        这就是著名的“开闭”原则：
            对扩展开放：允许新增 Animal 子类；
            对修改封闭：不需要修改依赖 Animal 类型的 run_twice() 等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。
'''

'''
静态语言 vs 动态语言
    对于静态语言（例如 Java）来说，如果需要传入 Animal 类型，则传入的对象必须是 Animal 类型或者它的子类，否则，将无法调用 run() 方法。
    对于 Python 这样的动态语言来说，则不一定需要传入 Animal 类型。只需要保证传入的对象有一个 run() 方法就可以了：
        class Timer(object):
            def run(self):
                print('Start...')

    这就是动态语言的 "鸭子类型"，它并不要求严格的继承体系，一个对象只要 "看起来像鸭子，走起路来像鸭子"，那它就可以被看做是鸭子。

    Python 的 "file-like object" 就是一种鸭子类型。对真正的文件对象，它有一个 read() 方法，返回其内容。
    但是，许多对象，只要有 read() 方法，都被视为 "file-like object"。
    许多函数接收的参数就是 "file-like object"，不一定要传入真正的文件对象，完全可以传入任何实现了 read() 方法的对象。
'''

'''
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
'''

# 除石头吃了不会跑的亏外，其余的都能 run，都是 "鸭子"，如下：
class Animal(object):   #编写Animal类
    def run(self):
        print("Animal is running...")

class Dog(Animal):  #Dog类继承Amimal类，没有run方法，有自己的eat方法
    def eat(self):
        print('Eating meat...')

class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
    def run(self):
        print('Cat is running...')

class Car(object):  #Car类不继承，有自己的run方法
    def run(self):
        print('Car is running...')

class Stone(object):  #Stone类不继承，也没有run方法
    pass

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
# Animal is running...
# Animal is running...

run_twice(Dog())
# Animal is running...
# Animal is running...

run_twice(Cat())
# Cat is running...
# Cat is running...

run_twice(Car())
# Car is running...
# Car is running...

run_twice(Stone())
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in run_twice
# AttributeError: 'Stone' object has no attribute 'run'