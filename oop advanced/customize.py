#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定制类
'''
__slots__ 变量，来限制该 class 实例能添加的属性，__len__() 方法是为了能让 class 作用于 len() 函数。
除此之外，Python 的 class 中还有许多这样有特殊用途的函数，可以帮助用来定制类。
'''


'''__str__'''
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('GaoFei'))
# <__main__.Student object at 0x100f8ce00>

'''
    定义好 __str__() 方法，返回一个好看的字符串就可以打印得好看并容易看出实例内部重要的数据：
'''
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
print(Student('GaoFei'))
# Student object (name: GaoFei)

'''
    直接敲变量不用 print，打印出来的实例还是老样子：
'''
s = Student('GaoFei')
s
# <__main__.Student object at 0x100f8ce00>

'''
    因为直接显示变量调用的不是__str__()，而是 __repr__()，两者的区别是 __str__() 返回用户看到的字符串，而__repr__() 返回程序开发者看到的字符串，也就是说，__repr__() 是为调试服务的。
    解决办法是再定义一个 __repr__()。但是通常 __str__() 和 __repr__() 代码都是一样的，所以，可以这样写：
'''
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


'''__iter__'''
'''
    如果一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实现一个 __iter__() 方法，该方法返回一个迭代对象，
    然后，Python 的 for 循环就会不断调用该迭代对象的 __next__() 方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环。

    以斐波那契数列为例，写一个 Fib 类，可以作用于 for循环：
'''
class Fib(object):
    def __init__(self, max_value=10000):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
        self.max_value = max_value

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值

        if self.a > self.max_value: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    
for n in Fib():
    print(n)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181
# 6765


'''__getitem__'''
'''
    Fib 实例虽然能作用于 for 循环，看起来和 list 有点像，但是，把它当成 list 来使用还是不行，比如，取第 5 个元素：
    要表现得像 list 那样按照下标取出元素，需要实现 __getitem__() 方法：
'''
Fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object is not subscriptable

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    
f = Fib()
f[0]
# 1
f[1]
# 1
f[2]
# 2
f[10]
# 89
f[100]
# 573147844013817084101

'''
    list 有个神奇的切片方法：
    对于 Fib 却报错。原因是 __getitem__() 传入的参数可能是一个 int，也可能是一个切片对象 slice，所以要做判断：
'''
list(range(100))[5:10]
# [5, 6, 7, 8, 9]

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
f[0:5]
# [1, 1, 2, 3, 5]
f[:10]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

'''
    但是没有对 step 参数作处理，也没有对负数作处理：
        f[:10:2]
        # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    此外，如果把对象看成 dict，__getitem__() 的参数也可能是一个可以作 key 的 object，例如 str。
    与之对应的是 __setitem__() 方法，把对象视作 list 或 dict 来对集合赋值。最后，还有一个 __delitem__() 方法，用于删除某个元素。

    总之，通过上面的方法，自定义的类表现得和 Python 自带的 list、tuple、dict 没什么区别，这归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
'''


'''__getattr__'''
'''
    正常情况下，当调用类的方法或属性时，如果不存在，就会报错。比如：
        调用 name 属性，没问题，但是，调用不存在的 score 属性，就有问题了：没有找到 score 这个 attribute
'''
class Student(object):
    def __init__(self):
        self.name = 'GaoFei'

s = Student()
print(s.name)
# GaoFei
print(s.score)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'

'''
    要避免这个错误，除了可以加上一个 score 属性外，Python 还有另一个机制，那就是写一个 __getattr__() 方法，动态返回一个属性。修改如下：
        当调用不存在的属性时，比如 score，Python 解释器会试图调用 __getattr__(self, 'score') 来尝试获得属性，这样，就有机会返回 score 的值：
        返回函数也可以：只是调用方式要变为：s.age()

    只有在没有找到属性的情况下，才调用 __getattr__，已有的属性，比如 name，不会在 __getattr__ 中查找。
'''
class Student(object):
    def __init__(self):
        self.name = 'GaoFei'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        
s = Student()
s.name
# 'GaoFei'
s.score
# 99

class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

s.age()
# 25

'''
    注意到任意调用如 s.abc 都会返回 None，这是因为定义的 __getattr__ 默认返回就是 None。要让 class 只响应特定的几个属性，就要按照约定，抛出 AttributeError 的错误：

    这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。实际作用就是，可以针对完全动态的情况作调用。
'''
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    
'''
    比如说：
        有些网站都搞 REST API，比如新浪微博、豆瓣，调用 API 的 URL 类似：
            http://api.server/user/friends
            http://api.server/user/timeline/list
        如果要写 SDK，给每个 URL 对应的 API 都写一个方法，而且，API 一旦改动，SDK 也要改。

        利用完全动态的 __getattr__，可以写出一个链式调用：
'''
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

Chain().status.user.timeline.list
# /status/user/timeline/list

'''
        这样，无论 API 怎么变，SDK 都可以根据 URL 实现完全动态的调用，而且，不随 API 的增加而改变！
        还有些 REST API 会把参数放到 UR L中，比如 GitHub 的 API：
            GET /users/:user/repos
        调用时，需要把 :user 替换为实际用户名。如果写出这样的链式调用：
            Chain().users('GaoFei').repos
        就可以非常方便地调用API了。
'''
class Chain(object):

    # 初始化一个路径变量 self._path，用于存储链式调用生成的路径
    def __init__(self, path=''):
        self._path = path

    # 动态添加路径部分。每次调用不存在的属性时，生成一个新的 Chain 实例，并将当前路径与新路径部分连接起来
    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    # 动态添加路径中的参数部分。每次调用实例时，生成一个新的 Chain 实例，并将当前路径与参数部分连接起来。
    # 如果有参数传入，将参数转换为字符串，并连接到当前路径。
    def __call__(self, *args):
        new_path = self._path
        if args:
            new_path = f'{self._path}/' + '/'.join(str(arg) for arg in args)
        return Chain(new_path)

    # 返回当前路径的字符串表示形式，以便打印时能够看到完整的路径
    def __str__(self):
        return self._path

    __repr__ = __str__

# 使用示例
print(Chain().status.user.timeline.list)  
# 输出: /status/user/timeline/list
print(Chain().users('GaoFei').repos)     
# 输出: /users/GaoFei/repos
print(Chain().api.v1.users('john').repos) 
# 输出: /api/v1/users/john/repos


'''__call__'''
'''
    一个对象实例可以有自己的属性和方法，当调用实例方法时，用 instance.method() 来调用。也可以直接在实例本身上调用。
    任何类，只需要定义一个 __call__() 方法，就可以直接对实例进行调用。示例：
'''
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('GaoFei')
s()
# My name is GaoFei.

'''
    __call__() 还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没什么根本的区别。
    如果把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，就模糊了对象和函数的界限。

    怎么判断一个变量是对象还是函数？更多的时候，需要判断一个对象是否能被调用，能被调用的对象就是一个 Callable 对象，比如函数和上面定义的带有 __call__() 的类实例：
'''
callable(Student())
# True
callable(max)
# True
callable([1, 2, 3])
# False
callable(None)
# False
callable('str')
# False


'''直白粗暴的记忆方法：__getattr__ 用于捕捉实例的属性 .xxx，__call__ 用于捕捉实例的调用 (xxx)。'''

'''其他可定制的方法，请参考/EXPAND/Special_method_names.md'''