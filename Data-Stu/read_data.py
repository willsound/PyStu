# @时间 : 2019-2-26 16:25 
# @作者 : 孙会想
# @文件 : read_data.py 
# @工具: PyCharm

import mysql.connector  # 导入库

config = {'host': '127.0.0.1',
          'user': 'root',
          'password': 'acdeff3811',
          'port': 3306,
          'database': 'python_data',
          'charset': 'gb2312'
          }
cnn = mysql.connector.connect(**config)
cursor = cnn.cursor()  # 获得游标
sql = "SELECT * FROM order_main"  # SQL语句
cursor.execute(sql)  # 执行sql语句
data = cursor.fetchall()  # 通过fetchall方法获得数据
for i in data[:2]:  # 打印输出前2条数据
    print (i)
cursor.close()  # 关闭游标
cnn.close()  # 关闭连接