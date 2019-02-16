

# 创建列表
names = ['Tom', 'Edison', 'Peter', 'Lucy']
age = [23, 45, 23, 26]
type(names)
type(age)

# 创建空列表
l = []
print(type(l), l, sep='\n')
l = list()
print(type(l), l, sep='\n')

# 转换其他数据结构为list
names = 'Tom, Edison'
list(names)

# 列表嵌套
member = [['Tom', 23], ['Peter', 40]]
member
type(member)


# 列表的操作
names = ['Tom', 'Edison', 'Peter', 'Lucy']

# 遍历
for name in names:
    print('I am', name)

# 列表长度
len(names)

# 检索
names[0]
names.index('Edison')
names[names.index('Edison')]

# 嵌套列表检索
member[0][1]

# 切片
names[0:3]
names[0:-1]

names[0:5]  # 索引可以溢出，这不同于字符串！

# # # 更新列表
# 修改元素
names[0] = '小强'

# 插入
names.insert(0, '小红')
names.insert(-3, 'Peter')

# 追加
names.append('小明')

# 扩展, 将可迭代对象的元素添加进列表中
names.extend('狗蛋')
names.extend(['狗蛋', '小樱'])

# 删除元素
# 1. 弹出, 一次只能弹出一个元素
names.pop(0)
names.pop(-1)

# 2. 删除, 可以一次删除多了元素
del names[0]
del names[6:9]

# 检查某元素是否在列表中
'狗蛋' in names
'小明' in names

# 计数
names.count('Peter')
names.count('peter')  # 没有，返回0

# 反转列表
names.reverse()
names[::-1]

# 复制列表
names1 = names
names.pop()
names1

# 弹出names的第一个元素之后，为什么names1也变了？
# 对象引用

# 那我们应该怎么复制一个列表？
names1 = names.copy()
names.insert(0, '小明')
names, names1

# 清空列
names1.clear()
names1




# 排序
# l.sort(key=None, reverse = False)
names
names.sort()
names
names.sort(reverse=True)
names

# sorted(iterable, key=None, reverse=False)
sorted(names)
sorted(names, reverse=True)




"""
推导式comprehensions（又称解析式），是Python的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 
Python共有三种推导：
1. 列表(list)推导式
2. 字典(dict)推导式
3. 集合(set)推导式
"""


# 列表推导式
# 列表推到/列表解析/列表展开，使用列表推导，将会一次产生所有结果。

# 已知一个列表，抽出它的偶数列表方法：
numbers = [1, 2, 3, 4, 5, 6]
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
print(even)

# 利用列表推导式：
numbers = [1, 2, 3, 4, 5, 6]
even = [number for number in numbers if number % 2 == 0]
print(even)


# 列表推导效率更高
import time

# 列表追加的方式
a = []
t0 = time.clock()
for i in range(1, 2000000):
    a.append(i)
print(time.clock() - t0, "seconds process time")
a_time = time.clock() - t0

# 列表推导式
t0 = time.clock()
b = [i for i in range(1, 2000000)]
print(time.clock() - t0, "seconds process time")
b_time = time.clock() - t0
print("method 2 is {} times quick than method 1!".format(a_time/b_time))
