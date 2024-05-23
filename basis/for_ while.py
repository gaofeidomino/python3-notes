#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环


# for...in 循环
# 依次把 list 或 tuple 中的每个元素迭代出来。把每个元素代入变量x，然后执行缩进块的语句
names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)
# Michael
# Bob
# Tracy

# 计算 1-100 的整数之和
# Python 提供一个 range() 函数，可以生成一个整数序列，再通过 list() 函数可以转换为 list。
list(range(5))
# [0, 1, 2, 3, 4]

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# 5050


# while 循环
# 只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 99

while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
# 在循环内部变量 n 不断自减，直到变为 -1 时，不再满足 while 条件，循环退出


# break
# 在循环中，break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行 break 语句
        break   # break 语句会结束当前循环
    print(n)
    n = n + 1
print('END')


# continue
# 也可以通过 continue 语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果 n 是偶数，执行 continue 语句
        continue    # continue 语句会直接继续下一轮循环，后续的 print() 语句不会执行
    print(n)
# 1
# 3
# 5
# 7
# 9


# 要特别注意，不要滥用 break 和 continue 语句。
# break 和 continue 会造成代码执行逻辑分叉过多，容易出错。
# 大多数循环并不需要用到 break 和 continue 语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉 break 和 continue 语句。

# 代码有问题，会让程序陷入“死循环”。这时可以用 Ctrl+C 退出程序，或者强制结束 Python 进程。