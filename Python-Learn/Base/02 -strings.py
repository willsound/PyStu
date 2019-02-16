


"""
单引号
双引号
三引号, 多行字符串，写的什么就打印出什么
r'Python \n is cool!', r在转义符前加上\，反转义
\
"""

s = 'Python 基础课程'
s = "Python 基础课程"

str1 = 'I love "Python"'
str2 = "I love 'Python'"
str3 = "I love \'Python\'"

s1 = '''Python 基础课程
\t
北京博宇通达科技有限公司
'''
s2 = r'Python 基础课程\n北京博宇通达科技有限公司'
print(s1, s2, sep='\n-----\n')

# print(value, ..., sep=' ', end='\n')
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.

# str(x) 将对象x转换为字符串
str(123)

# chr(x) 将一个整数转换为它在Unicode编码中对应的字符
chr(1)
chr(97)

# ord(x) 将一个字符转换为它在Unicode编码中对应的整数值
ord('a')
ord('你')


# 检索
s[3]
s[-3]

len(s)
s[20]  # 索引不能溢出


# 切片
s[0:6]
s[-3]
s[0:-5]
s[:]
s

# 创造一个与原字符串顺序相反的字符串
s[::-1]

# 字符串相关操作
s = 'Python' + '基础课程'
s = 'Python' '基础课程'
s = 'abc' * 3

l = ['Python', '基础课程']
' '.join(l)

# 判断元素是否在序列之内
'a' in s

len(s)  # 字符串的长度，字符个数
max(s)  # 按字母排序后的最后一个
min(s)  # 按字母排序后的第一个


s = ' this Is a string. Yes, it is!   '
print(s)
print(s.capitalize())  # 第一个单词的首字母大写
print(s.title())       # 每个单词首字母大写
print(s.upper())       # 大写
print(s.lower())       # 小写
print(s.swapcase())    # 小写转成大写，大写转成小写

print(s.find('is'))    # 找不到时返回-1
print(s.index('iS'))   # 找不到时报错
# rfind(), rindex()

print(s.replace('this', 'that'))
print(s.strip())
s.split()

s = s.strip()
# lstrip(), rstrip()

s.endswith('!')
s.startswith('t')
s.startswith('t', 3, 6)    # s[3:6]
s.startswith('t', 11, 15)  # s[11:15]


'a'.islower()
'A'.isupper()

print(s.isdigit())
print(s.isalpha())
print(s.isalnum())

'1234'.isdigit()
'1234再来一次'.isdigit()
'再来一次'.isalpha()
'1234再来一次'.isalpha()
'1234再来一次'.isalnum()

print(s.isprintable())
'\t'.isprintable()


# python3 中字符串以unicode形式存储，字符串转化成字节码需要前面加b
s = "Python 基础课程"
# 编码
s1 = s.encode('utf-8')
print(s1)
# 解码
s2 = s1.decode('utf-8')
print(s2)


# format 方法
name, age, job = 'Tom', 20, 'Dev'

print('姓名：'+name+'，年龄'+str(age)+',工作:'+job)
print('姓名：{}，年龄：{}，工作：{}'.format(name, age, job))
print('姓名：{0}，年龄：{1}，工作：{2}'.format(name, age, job))
# 添加元素：
'姓名：{0}，年龄：{1}，工作：{2}，部门：{department}'.format(name, age, job, department='tech')

# 占位符
# {0:10}, 0表示format方法中序列的索引，10表示位置长度
'{0:10} = {1:10}'.format('美库尔信息咨询', 123.4567)  # 默认字符靠左对齐，数字靠右对齐
# '美库尔信息咨询    =   123.4567'

# 对齐方式
'{0:>10} = {1:<10}'.format('美库尔信息咨询', 123.4567)
# '   美库尔信息咨询 = 123.4567  '

'正在抓取第{1:10}个产品：{}'.format('皇家狗粮一号', 12345)
# ValueError: cannot switch from manual field specification to automatic field numbering
# '正在抓取第{1:10}个产品：{0}'.format('皇家狗粮一号',12345)


# 指定数字格式
'{},{},{}'.format(3.14159, 3.14159, 3.14159)
'{1:f},{0:.2f},{2:06.2f}'.format(3.14159, 2.14159, 1.14159)
# '2.141590,3.14,001.14'


# 相关的包
import string
# 26个字母
string.ascii_letters
# 26个大写字母
string.ascii_uppercase
# 26个小写字母
string.ascii_lowercase

# 标点符号
string.punctuation
