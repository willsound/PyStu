import os


# 切换当前工作路径
path = r'C:\Darren\ziqing\Merkle\Python\base\文件处理'
os.chdir(path)


# 打开文件
f = open('lines.txt')       # 默认以只读模式打开文件，如果文件不存在则创建
f = open('lines.txt', 'w')  # 以写模式打开, 如果文件不存在则创建

# 关闭文件句柄
f.close()

# 文件的读取模式， open() 返回文件流
# read([size])  # size表示字符个数
# readline([size])
# readlines([size])

# 读入整个文件
print(f.read())
f = open('文件处理\lines.txt')
print(f.read(2))  # 返回文件中前两个字符

# 读入一行
f = open('文件处理\lines.txt')
print(f.readline())
print(f.readline(2))  # 返回行中前两个字符

# 读入所有文件，按行以list形式返回
f = open('文件处理\lines.txt')
print(f.readlines())
print(f.readlines(30))
# 这里的size不如上面的严格， 如果size小于第一行的字符数，则返回第一行，
# 如果大于第一行的字符数又小于前两行的总字符数，则返回前两行，以此类推

# 检查打开的文件对象是否可读
f.readable()


# 文件的写入模式

# w:只写模式, 文件必须存在 # # # # # # #
f2 = open('write.txt', 'w')
# f2 = open('write.txt')

# write(str)
f2.write('hello world!')

# writelines(字符串序列)
f2.writelines(['hey', 'I am Python'])

# 将缓存数据写入文件
f2.flush()

# 检查打开的文件对象是否可写
f2.writable()

f2.close()


# w+:删除原内容并以读写模式,如果文件不存在则创建 #
f2 = open('write.txt', 'w+')
# f2 = open('write.txt')

# write(str)
f2.write('hello world!')
# writelines(字符串序列)
f2.writelines(['hey', 'I am Python'])

f2.read()

# 将缓存数据写入文件
f2.flush()
f2.read()  # 刷新之后还是不能读取内容

# 检查打开的文件对象是否可写
f2.writable()

f2.close()


# 以追加模式打开文件，文件指针在文件末尾，如果文件不存在则创建
f = open('test.txt', 'a')
f = open('test.txt', 'a+')  # 追加+可读写模式打开，指针在文件末尾，必须的重置指针位置才能读取到内容
f.writelines(['append the text in another line.',
              'append the text in another line.',
              'append the text in another line.'])

# 将缓存数据写入文件
f.flush()

# 追加模式不可读
f.readable()

f.write('new line')

f.close()


# 以读模式打开文件，rb为二进制模式(如图片或可执行文件等)
f = open('test.txt', 'rb')
print(f.read())

f = open('merkle.jpg', 'rb')  # 不能以文本模式读取图片
print(f.read())


# 另一种写法（推荐），会自动关闭文件句柄
with open('test.txt', 'r') as f:
    print(f.read())
