

a = 1
b = -10.3

# 查看变量类型
type(a)
type(b)
# 变量类型转换
c = float(a)
type(a)

# 删除变量
del a, b

# 科学计数法
3.14e5

# 二进制, 0b
a = 0b1010
# 八进制, 0o
b = 0o110
# 十六进制, 0x
c = 0x110f

# 注意这里只是用不同进制定义了十进制数
id(a) == id(10)

# 进制之间转化, int(), float(), bin(), oct(), hex()
# int(x [,base=m]) 将x转换为一个m进制的整数 （默认为10）
int()  # 无参数是返回0
int(a)
int(b'12', base=8)  # 将字节所对应的base进制数转化为十进制数， base可以为8， 10， 16
int('0b1010', base=2)    # 将字符串所对应的base进制数转化为十进制数， base可以为8， 10， 16

# float(x) 将x转换到一个浮点数
float(123)

# bin(x) 将x转换到一个二进制数字符串
bin(a)

# oct(x) 将x转换到一个八进制数字符串
oct(a)

# hex(x) 将x转换到一个十六进制数字符串
hex(a)


# 数学运算，加+，减-，乘*，除/， 乘方**，整除//，取余(模)%
(50 - 5*6)/4

8 / 4  # 除法总是返回浮点数

17 // 3
17 % 3

# 相关函数
abs(-10.8)
max(1, 2, 3)
min(1, 2, 3)
pow(2, 5)
round(-3.1415926)
round(-3.1415926, 0)
round(-3.1415926, 3)


# 数字相关的包/模块
import math

pi = math.pi
e = math.e

# 向上取整
math.ceil(pi)
# 向下取整
math.floor(pi)
# 向0的方向取整
math.trunc(pi)
# 开方
math.sqrt(pi)
# 指数
math.exp(10)
# 对数
math.log(10)
math.log2(10)
math.log10(10)


0.1 + 0.1 + 0.1 - 0.3
# 5.551115123125783e-17  # 二进制浮点数表示


# 十进制浮点数
from decimal import *
from decimal import Decimal

Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')

# Decimal表示方法
Decimal(0.12)  # 二进制浮点数表示
Decimal('0.12')
Decimal((0, (3, 1, 4), -2))  # 0表示正数字, 1表示负号; 元组，只能包含数字；科学计数法E后的数字

Decimal(str(2.0 ** 0.5))
Decimal('2') ** Decimal(0.5)
Decimal('2') ** Decimal('0.5')
Decimal(2.0 ** 0.5)

# 设定精度
getcontext().prec
Decimal(1) / Decimal(7)

getcontext().prec = 6
Decimal(1) / Decimal(7)


# 相关函数
# 开方
Decimal(2).sqrt()
Decimal.sqrt(Decimal(2))

# 指数
Decimal(1).exp()

# 对数
Decimal('2.7').ln()
Decimal('10').log10()

# 比较大小
Decimal('2').max(Decimal('3'))

Decimal.max(Decimal('3'), Decimal('2'))

Decimal('2').min(Decimal('3'))
Decimal.min(Decimal('3'), Decimal('2'))
