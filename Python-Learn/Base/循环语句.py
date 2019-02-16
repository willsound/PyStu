


# 循环语句

# 1. for 语句和控制流程
# 打印20以内的质数
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    # 当循环正常结束时执行
    else:
        print(n, '是质数！')


# 2. while 语句和控制流程
a, b = 0, 1
while b < 100:
    print(b, end=',')
    a, b = b, a+b


i, j = 0, 1
while True:
    print(i+j)
    i, j = i + j, i
    if i >= 10:
        break

i, j = 0, 1
while i < 10:
    print('{} + {} ='.format(i, j), i+j)
    if i == 3:
        print('i ==', i)
        i += 1
        continue
    i, j = i + j, i
    if i == 6:
        print('i ==', i)
        break
# 当循环正常结束时执行
else:
    print('不是以因为break结束！')
