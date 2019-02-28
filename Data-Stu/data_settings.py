from matplotlib.font_manager import FontProperties


class DataSettings():
    def __init__(self):
        self.data_file_path = r'Data\data.txt'
        self.data_cluster_file_path = r'Data\cluster.txt'
        self.data_regression_file_path = r'Data\regression.txt'
        self.font_file_path = r'Resources\msyh.ttc'
        self.font_title = FontProperties(fname=self.font_file_path, size=14)
        self.font_xlable = FontProperties(fname=self.font_file_path, size=10)
        self.font_ylable = FontProperties(fname=self.font_file_path, size=10)


class MysqlSettings():
    def __init__(self):
        self.conn_host = '127.0.0.1'
        self.conn_user = 'root'
        self.conn_password = 'acdeff3811'
        self.conn_port = '3306'
        self.conn_database = 'python_data'
        self.conn_charset = 'gb2312'