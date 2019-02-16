


# 定义：含任意对象的不可变有序集合
# 创建：
t = ('Jerry', 'Tom', 23)
t = 'Frogs', 'Hogs', 'Dogs', 'Logs'
t = ('Jerry')
type(t)
# 创建仅有一个元素的元组
t = ('Jerry', )       # 只有一个元素时，必须以“，”结束，否则视为创建字符串或数字
t = tuple([1, 2, 3])  # 转list 为 tuple

# 空元组
()
tuple()

# 嵌套
t = ('Jerry', (1, 2, 3), ['a'])
t
type(t)


# 常用操作
t = ('Frogs', 'Hogs', 'Dogs', 'Logs')

# 通过下标索引/位置偏移来访问元素, 同列表
t[0]
t[0:3]

# 返回元素索引
t.index('Dogs')

# 计数
t.count('Dogs')

# 连接 +
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
t1 + t2

# 重复 *
t1 * 3
