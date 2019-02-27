# @时间 : 2019-2-27 13:24 
# @作者 : 孙会想
# @文件 : mysqltest.py 
# @工具: PyCharm

import data_settings
import read_data as rd
my_mysql=data_settings.MysqlSettings()
my_conn=rd.conn_database_mysql(my_mysql.conn_host,my_mysql.conn_database,my_mysql.conn_user,my_mysql.conn_password)
my_mysql_cursor=my_conn.cursor()

sql = "SELECT * FROM order_main order by order_id limit 10"  # SQL语句
my_mysql_cursor.execute(sql)  # 执行sql语句
data = my_mysql_cursor.fetchall()  # 通过fetchall方法获得数据
for i in data[:]:  # 打印输出前2条数据
    print (i)
my_mysql_cursor.close()  # 关闭游标
my_conn.close()  # 关闭连接