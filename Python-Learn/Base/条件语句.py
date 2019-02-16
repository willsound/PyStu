


# 条件判断语句

# 1. 条件执行
# 1.1 if...else
x = int(input('please input a number:'))
if x > 3:
    print("x bigger than 3!")
else:
    print('x less than 3!')

# 1.2 if...elif...else
# 'elif' 是 'else if'的缩写
x = int(input('please input a number:'))
if x > 3:
    print("x bigger than 3!")
elif x == 3:
    print("x ==3")
else:
    print('x less than 3!')

# 2. 条件表达式
a, b = 0, 1
s = 'Hey' if a < b else 'Bye~'
s
