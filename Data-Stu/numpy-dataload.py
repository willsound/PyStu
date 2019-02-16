# 2. 使用Numpy的loadtxt、load、fromfile读取数据
import numpy as np  # 导入numpy库
file_name = r'Data\numpy_data.txt'  # 定义数据文件
data = np.loadtxt(file_name, dtype='float32', delimiter=' ')  # 获取数据
print(data)  # 打印数据



'''
import numpy as np  # 导入numpy库
write_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 定义要存储的数据
np.save('load_data', write_data)  # 保存为npy数据文件
read_data = np.load('load_data.npy')  # 读取npy文件
print (read_data)  # 输出读取的数据

import numpy as np  # 导入numpy库
file_name = 'numpy_data.txt'  # 定义数据文件
data = np.loadtxt(file_name, dtype='float32', delimiter=' ')  # 获取数据
tofile_name = 'binary'  # 定义导出二进制文件名
data.tofile(tofile_name)  # 导出二进制文件
fromfile_data = np.fromfile(tofile_name, dtype='float32')  # 读取二进制文件
print (fromfile_data)  # 打印数据
'''