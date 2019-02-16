


import csv

# 读取 csv 文件
with open('文件处理/test-1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 写入 csv 文件
with open('文件处理/test-2.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=','
                            , quotechar='"'  # 将含有特殊字符的字段用"引起来, 只允许指定一个字符, 默认是双引号
                            , quoting=csv.QUOTE_MINIMAL  # 将含有特殊字符的字段用"（双引号）引起来, 默认方式
                            # , quoting=csv.QUOTE_ALL  # 将所有的字段用"（双引号）引起来
                            # , quoting=csv.QUOTE_NONNUMERIC  # 将非数字的的字段用"（双引号）引起来
                            # , quoting=csv.QUOTE_NONE  # 所有字段都不用"（双引号）引起来， 不推荐
                            )
    csv_writer.writerow(['name', 'age', 'job title'])
    csv_writer.writerows([['小明', 27, '高级，分析师'],
                          ['小红', 18, '分析师助理']])


with open('文件处理/test-2.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['name', 'age', 'job title'])
    csv_writer.writerows([['小明', 27, '高级分析师'],
                          ['小红', 18, '分析师助理']])

# 默认的情况下, 读和写使用逗号做分隔符(delimiter)，用双引号作为引用符(quotechar)，当遇到特殊情况是，可以根据需要手动指定字符
# 指定冒号作为分隔符，并且指定quote方式为不引用。这意味着读的时候都认为内容是不被默认引用符(")包围的
with open('文件处理/test-3.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

with open('文件处理/test-32.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)  # QUOTE_NONE
    for row in reader:
        print(row)


# csv还提供了一种类似于字典方式的读写，方式如下:

# 读
f = open("文件处理/test-2.csv", encoding='utf-8')  # csv 也是文本文件，只是用逗号做分隔符，是比较常用的一种格式而已
for row in csv.DictReader(f):
    print(row['name'], row['age'])

f.close()

with open('文件处理/test-2.csv', 'r', encoding='utf-8') as csvfile:
    for row in csv.DictReader(csvfile):
        print(row['job title'])


# 写
with open('文件处理/test-1.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'middle_name': 'Wonderful', 'last_name': 'Spam'})
    writer.writerows([{'first_name': 'Adam', 'last_name': 'Lundgren'},
                      {'first_name': 'Joel', 'last_name': 'Li'}])
