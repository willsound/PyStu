# @时间 : 2019-2-26 16:25 
# @作者 : 孙会想
# @文件 : read_data.py 
# @工具: PyCharm

import mysql.connector

def conn_database_mysql(conn_host,conn_database,conn_user,conn_password,conn_port='3306',conn_charset='gb2312'):
    conn_config = {'host': conn_host,
                  'user': conn_user,
                  'password': conn_password,
                  'port': conn_port,
                  'database': conn_database,
                  'charset':conn_charset
                  }
    return mysql.connector.connect(**conn_config)



