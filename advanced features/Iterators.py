#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代器
'''
可以直接作用于for循环的数据类型有以下几种：
    一类是集合数据类型，如list、tuple、dict、set、str等；
    一类是generator，包括生成器和带yield的generator function
'''

'''
⚠️⚠️⚠️ 可以直接作用于for循环的对象统称为 「可迭代对象：Iterable」
'''

# 可以使用 isinstance() 判断一个对象是否是 Iterable 对象
from collections.abc import Iterable

isinstance([], Iterable)
# True

isinstance({}, Iterable)
# True

isinstance('abc', Iterable)
# True

isinstance((x for x in range(10)), Iterable)
# True

isinstance(100, Iterable)
# False

# 生成器不但可以作用于 for 循环，还可以被 next() 函数不断调用并返回下一个值，直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。

'''
⚠️⚠️⚠️ 可以被 next() 函数调用并不断返回下一个值的对象称为「迭代器：Iterator」
'''

# 可以使用 isinstance() 判断一个对象是否是 Iterator 对象：
from collections.abc import Iterator

isinstance((x for x in range(10)), Iterator)
# True

isinstance([], Iterator)
# False

isinstance({}, Iterator)
# False

isinstance('abc', Iterator)
# False

# 生成器 Generators 是一种特殊类型的「迭代器：Iterator」，它们是通过使用 yield 关键字来生成值的函数。
'''
因此，生成器是迭代器的一种。
'''
# 迭代器（Iterators）是一个对象，它可以被遍历（或者说迭代），并且可以逐个返回其元素。
# 生成器是一种惰性的方式来生成序列，它可以被看作是一种特殊的迭代器。

# list、dict、str 虽然是 「可迭代对象：Iterable」，却不是 「迭代器：Iterator」。
# 把 list、dict、str 等 「可迭代对象：Iterable」 变成 「迭代器：Iterator」 可以使用 iter() 函数：
isinstance(iter([]), Iterator)
# True

isinstance(iter('abc'), Iterator)
# True

'''
为什么 list、dict、str 等数据类型不是 Iterator？
    这是因为 Python 的 迭代器：「迭代器：Iterator」 对象表示的是一个数据流，「迭代器：Iterator」 对象可以被 next() 函数调用并不断返回下一个数据，直到没有数据时抛出 StopIteration 错误。
    可以把这个数据流看做是一个有序序列，但不能提前知道序列的长度，只能不断通过 next() 函数实现按需计算下一个数据，所以 「迭代器：Iterator」 的计算是惰性的，只有在需要返回下一个数据时它才会计算。

 「迭代器：Iterator」甚至可以表示一个无限大的数据流，例如全体自然数。而使用 list 是永远不可能存储全体自然数的。
'''



# 小结
# 凡是可作用于 for 循环的对象都是 Iterable 类型；
# 凡是可作用于 next() 函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列；
# 集合数据类型如 list、dict、str 等是 Iterable 但不是 Iterator，不过可以通过 iter() 函数获得一个 Iterator 对象。

# Python 的 for 循环本质上就是通过不断调用 next() 函数实现的，例如
for x in [1, 2, 3, 4, 5]:
    pass

# 实际上等价于

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


'''
可迭代对象（Iterable）：可迭代对象是指那些可以返回一个迭代器的对象。
    任何实现了 __iter__() 方法的对象都是可迭代对象。
    可迭代对象可以用于在循环中逐个访问其元素，或者被传递给 iter() 函数来获得一个迭代器。

迭代器（Iterators）：迭代器是一个对象，它实现了 __iter__() 和 __next__() 方法。
    __iter__() 方法返回迭代器自身，而 __next__() 方法用于返回序列中的下一个元素。
    当没有元素时，__next__() 方法应该触发一个 StopIteration 异常。迭代器通常被用于循环中来逐个访问序列中的元素。
'''

# 举例来说，一个列表是一个可迭代对象，因为可以通过调用 iter() 函数来获得一个迭代器，然后使用 __next__() 方法来逐个访问列表的元素。
my_list = [1, 2, 3]
my_iterator = iter(my_list)  # 获得一个迭代器

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# 1
# 2
# 3

# 总的来说，可迭代对象是那些可以被迭代的对象，而迭代器则是负责实际迭代的对象。

'''
__iter__() 和 __next__() 是 Python 中迭代器协议的两个特殊方法（双下划线方法），用于实现迭代器的行为。

__iter__() 方法：
    当对象调用 iter() 函数时，会返回一个迭代器对象。这个迭代器对象通常是自身，即返回 self。
    如果一个对象实现了 __iter__() 方法，那么它就是一个可迭代对象（Iterable）。

__next__() 方法：
    当调用 next() 函数时，会触发这个方法，返回序列中的下一个元素。
    如果没有更多的元素可供迭代，那么这个方法应该触发一个 StopIteration 异常。
'''

# 实现一个简单的迭代器来生成一个序列
class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.max_value:
            self.current_value += 1
            return self.current_value
        else:
            raise StopIteration

# 使用自定义的迭代器来生成一个序列
my_iterator = MyIterator(5)

for value in my_iterator:
    print(value)

# 在这个例子中，MyIterator 类实现了 __iter__() 和 __next__() 方法，从而成为一个迭代器。
# __iter__() 方法返回自身，而 __next__() 方法实现了返回序列中的下一个值，并在序列结束时触发 StopIteration 异常。