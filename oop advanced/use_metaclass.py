#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用元类 eg: SAMPLES/orm.py
'''
type()
    动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
    比方说要定义一个 Hello 的 class，就写一个 hello.py 模块（SAMPLES/hello.py）：
        class Hello(object):
            def hello(self, name='world'):
                print('Hello, %s.' % name)
        当 Python 解释器载入 hello 模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个 Hello 的 class 对象，测试如下：
'''
from hello import Hello
h = Hello()
h.hello()
# Hello, world.
print(type(Hello))
# <class 'type'>
print(type(h))
# <class 'hello.Hello'>

'''
    type() 函数可以查看一个类型或变量的类型，Hello 是一个 class，它的类型就是 type，而 h 是一个实例，它的类型就是 class Hello。

    class 的定义是运行时动态创建的，而创建 class 的方法就是使用 type() 函数。

    type() 函数既可以返回一个对象的类型，又可以创建出新的类型，比如，可以通过 type() 函数创建出 Hello 类，而无需通过 class Hello(object)... 的定义：
'''
def  fn(self, name="world"): # 先定义函数
    print('Hello, %s.' % name )

Hello =  type("Hello", (object,), dict(hello=fn))   # 然后用 type 来创建新类型 Hello class

h = Hello()
h.hello()
# Hello, world.
print(type(Hello))
# <class 'type'>
print(type(h))
# <class '__main__.Hello'>  
# # __main__表示当前这个Python文件正在被执行

'''
    要创建一个 class 对象，type() 函数依次传入 3 个参数：
        class 的名称；
        继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，别忘了 tuple 的单元素写法；
        class 的方法名称与函数绑定，这里把函数 fn 绑定到方法名 hello 上。

    通过 type() 函数创建的类和直接写 class 是完全一样的，因为 Python 解释器遇到 class 定义时，仅仅是扫描一下 class 定义的语法，然后调用 type() 函数创建出 class。

    正常情况下，都用 class Xxx... 来定义类，但是，type() 函数也允许动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，
    这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''


'''
metaclass
    除了使用 type()动态创建类以外，要控制类的创建行为，还可以使用 metaclass。

    metaclass，直译为元类，简单的解释就是：
        当定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
        但是如果想创建出类呢？那就必须根据 metaclass 创建出类，所以：先定义 metaclass，然后创建类。
        连接起来就是：先定义 metaclass，就可以创建类，最后创建实例。
    所以，metaclass 允许创建类或者修改类。换句话说，可以把类看成是 metaclass 创建出来的“实例”。

    metaclass 是 Python 面向对象里最难理解，也是最难使用的魔术代码。正常情况下，不会碰到需要使用 metaclass 的情况。

    看一个简单的例子，这个 metaclass 可以给自定义的 MyList 增加一个 add 方法：
        定义 ListMetaclass，按照默认习惯，metaclass 的类名总是以 Metaclass 结尾，以便清楚地表示这是一个 metaclass：
'''
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):     # cls 指的是本类
        attrs['add'] =  lambda self, value: self.append(value)      # 添加新的方法
        return type.__new__(cls, name, bases, attrs)
    
'''
        有了 ListMetaclass，在定义类的时候还要指示使用 ListMetaclass 来定制类，传入关键字参数 metaclass：
'''
class myList(list, metaclass=ListMetaclass):
    pass

'''
        当传入关键字参数 metaclass 时，魔术就生效了，它指示 Python 解释器在创建 MyList 时，要通过 ListMetaclass.__new__() 来创建，在此，可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

        __new__() 方法接收到的参数依次是：
            当前准备创建的类的对象；
            类的名字；
            类继承的父类集合；
            类的方法集合。

        测试一下 MyList 是否可以调用 add() 方法：
        而普通的 list 没有 add() 方法：
'''
L = myList()
L.add(1)
L
# [1]

l2 = list()
l2.add(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'add'


'''
动态修改有什么意义？直接在 MyList 定义中写上 add() 方法不是更简单吗？正常情况下，确实应该直接写，通过 metaclass 修改纯属变态。
但是，总会遇到需要通过 metaclass 修改类定义的。ORM 就是一个典型的例子。

ORM 全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作 SQL 语句。
要编写一个 ORM 框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

尝试编写一个ORM框架。
    编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个 ORM 框架，想定义一个 User 类来操作对应的数据库表 User，期待写出这样的代码：
        其中，父类 Model 和属性类型 StringField、IntegerField是由 ORM 框架提供的，剩下的魔术方法比如 save() 全部由父类 Model 自动完成。
        虽然 metaclass 的编写会比较复杂，但 ORM 的使用者用起来却异常简单。
'''
class User(Model): # type: ignore
    # 定义类的属性到列的映射：
    id = IntegerField('id') # type: ignore
    name = StringField('username') # type: ignore
    email = StringField('email') # type: ignore
    password = StringField('password') # type: ignore

# 创建一个实例：
u = User(id=123, name='Michael', email='test@orm.org', password='my-pwd')
# 保存
u.save()


'''
    实现 ORM。首先来定义 Field 类，它负责保存数据库表的字段名和字段类型：
    在 Field 的基础上，进一步定义各种类型的 Field，比如 StringField，IntegerField 等等：
'''
class  Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return  '<%s:%s>' % (self.__class__.__name__ , self.name)
    
class StringField(Field):
    def  __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

'''
    下一步，就是编写最复杂的 ModelMetaclass 了：
    以及基类 Model：
'''
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
             return type.__new__(cls, name, bases, attrs)
        
        print('Found model: %s' % name)

        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__']  = name # 假设表名和类名一致

        return type.__new__(cls, name, bases, attrs)
    
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 什么是 ','.join(fields)
# 是一个字符串方法，用于将一个可迭代对象 fields 中的元素连接成一个字符串，每个元素之间用逗号分隔。
# 具体来说，','.join(fields) 的返回值是一个由 fields 中的元素组成的字符串，元素之间用逗号分隔，例如：
# fields = ['id', 'name', 'email', 'password']
# result = ','.join(fields)
# print(result)  # 'id,name,email,password'
# 在这行代码中，','.join(fields) 的作用是将 fields 列表中的列名连接成一个字符串，用于构造 SQL 语句中的列名部分。

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id') # type: ignore
    name = StringField('username') # type: ignore
    email = StringField('email') # type: ignore
    password = StringField('password') # type: ignore

'''
    当用户定义一个 class User(Model) 时，Python 解释器首先在当前类 User 的定义中查找 metaclass，
    如果没有找到，就继续在父类 Model 中查找 metaclass，找到了，就使用 Model 中定义的 metaclass 的 ModelMetaclass 来创建 User 类，
    也就是说，metaclass 可以隐式地继承到子类，但子类自己却感觉不到。

    在 ModelMetaclass 中，一共做了几件事情：
        排除掉对 Model 类的修改；
        在当前类（比如 User）中查找定义的类的所有属性，如果找到一个 Field 属性，就把它保存到一个 __mappings__ 的 dict 中，
            同时从类属性中删除该 Field 属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
        把表名保存到 __table__ 中，这里简化为表名默认为类名。

    在 Model 类中，就可以定义各种操作数据库的方法，比如 save()，delete()，find()，update 等等。
    实现了 save() 方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出 INSERT 语句。

    测试如下：
        save() 方法已经打印出了可执行的 SQL 语句，以及参数列表，只需要真正连接到数据库，执行该 SQL 语句，就可以完成真正的功能。
'''
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# Found model: User
# Found mapping: id ==> <IntegerField:id>
# Found mapping: name ==> <StringField:username>
# Found mapping: email ==> <StringField:email>
# Found mapping: password ==> <StringField:password>

u
# {'id': 12345, 'name': 'Michael', 'email': 'test@orm.org', 'password': 'my-pwd'}

dir(u)
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__mappings__', 
# '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', 
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__table__', '__weakref__', 
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'save', 'setdefault', 'update', 'values']

u.__table__
# 'User'
u.__mappings__
# {
#     'id': <__main__.IntegerField object at 0x1048bae70>, 
#     'name': <__main__.StringField object at 0x1048baed0>, 
#     'email': <__main__.StringField object at 0x1048baea0>, 
#     'password': <__main__.StringField object at 0x1048baf30>
# }

u.save()
# SQL: insert into User (id,username,email,password) values (?,?,?,?)
# ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']



'''
流程是这样的。user 父类是 model, model 的元类是 metamodel。
    所以首先要根据元类创建类，先是 user 类的父类 model 会去执行一下元类的 new 方法，之后才是 user 类去执行元类 new 方法。
    所以过程中其实执行了两次 new。model 类一般不需要变动所以直接不进行任何处理创建类，关键在于 user 类本身那些类属性需要进行改动
    （  
        说白了就是将人为个性化因素都放到 mapping 里，这里可能会问不特意放 mapping 里不行吗？
        元类核心就是这个 mapping，因为需要的是 field 类属性也就是数据库的那些列，除此之外其实还有很多很多不相关系统属性或方法名。
        那怎么判断是不是想要的？
        那就是提前判断处理把它们集中放到 mapping 里后续只需要围绕 mapping 展开，同时去掉 user 类中的相关属性不然这些属性会覆盖 mapping 中的，
        这里所说的人为化因素是指 user 类中的类属性等号左边，用户可以给不同的命名，右边是数据库中的列属性名称用户不可更改
    ）

    执行两次元类的 new 之后类就创建好了，注意前面两次 new 的改动针对的都是类变量不是实例变量，此时还没实例化。
    下一步就是类实例对象的创建，我们知道创建对象要初始化操作，而 user 类中没有 __init__ 方法，此时就会执行副类 moedel 中 的__init__，
    那其实 model 中的 __init__ 调用的是它的副类 dict 的初始化操作，所以该对象本身最终就是一个字典，内容是创建实例对象时括号里的内容。

实例话后接下来开始执行 save()，要做的就是自定义属性名对应的值和数据库对应列对应起来。

ps：对与 getattr(self, k, none) 这个方法一开始我特别疑惑，因为实例对象是一个字典比如 id 对应 1234, 为什么四次遍历全都为 false 找不到呢？
    于是我猜测这个方法的第一个参数应该是 self 对应的类类型，是指 User 类，而不是指该类的实例对象。
    所以这和实例对象是不是字典，字典里有没有对应值无关，user 类属性确实没有，
    因为执行元类时都放到 mapping 里了就没有这些属性了，而 __getattr__ 方法中的 self[k] 可以取到是因为这里的 self 是指具体的实例对象，是一种字典下标去治。
'''