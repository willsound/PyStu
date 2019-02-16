


# 创建字典
d = {'guido': 4127, 'sape': 123, 'jack': 4098}
d

d = dict([('guido', 4127), ('sape', 123), ('jack', 4098)])
d

# 创建空字典
{}
dict()

d1 = dict.fromkeys(['a', 'b', 'c'], 3357)
d1

dict.fromkeys('fsdf', 'f')
# {'d': 'f', 'f': 'f', 's': 'f'}
dict.fromkeys('fsd', ['f',23])
# {'d': ['f', 23], 'f': ['f', 23], 's': ['f', 23]}
dict.fromkeys(['fsdf'], ['f'])
# {'fsdf': ['f']}


# 字典的嵌套
response = {"attributionURL": "http://www.glassdoor.com/Job/us-merkle-jobs-SRCH_IL.0,2_IN1_KE3,9.htm",
            "countReturned": 0,
            "cities": [
                {"numJobs": 46,
                 "name": "New York, NY",
                 "latitude": 40.71417,
                 "longitude": -74.00639
                 },
                {"numJobs": 43,
                 "name": "Columbia, MD",
                 "id": 1153546,
                 "latitude": 39.24028,
                 "longitude": -76.83972
                 }]
            }


# 字典长度
len(d)

# 检索
d['guido']


d.setdefault('tom')  # 返回tom的值，如果tom不在字典中，在将tom加入，值设置为None
d
d.setdefault('Tom', 2344)  # 返回tom的值，如果tom不在字典中，在将tom加入，值设置为2344
d

d.setdefault('sape')

# 获取键
d.keys()

# 获取值
d.values()

# 获取所有元素
d.items()

# 遍历字典
for k, v in d.items():
    print('key is {}, value is {}'.format(k, v))

# # #更新字典
# 添加键值对
d['Tom'] = 5423

# 弹出元素
d.pop('guido')  # 必须指定键
d

d.pop('tom')  # 如果没有该键，报错

# 弹出键值对
d.popitem()

# 更新字典
d.update({'Tom': 1234})

# 判断键是否在字典中
'Tom' in d

# 复制字典
d1 = d

d1 = d.copy()

# 删除字典中的键值对
del d['Tom']
# 清空字典
d.clear()

# 删除字典
del d


# 字典推导式
import string

lyric = '''Merkle is a global data-driven, technology-enabled performance marketing agency.
 Performance marketing focuses on measurable outcomes.
 At Merkle, we help brands make the people-based marketing transformation.
'''

# 分词，移除标点符号
words = [word.strip(string.punctuation).lower() for word in lyric.split()]
print(len(words), words)

# 关键字提取
words_index = set(words) - {'a', 'is', 'on', 'the', 'at'}
print(len(words_index), words_index)

# 通过字典推导式生成字典
counts_dict = {index: words.count(index) for index in words_index}
print(counts_dict)

# 计算keys的最大长度
max([len(k) for k in counts_dict.keys()])  # 列表推导式
# 按关键字出现频次由高到低打印
for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{:20} -- {} times'.format(word, counts_dict[word]))
