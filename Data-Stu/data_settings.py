from matplotlib.font_manager import FontProperties


class Settings():
    def __init__(self):
        self.data_file_path = r'Data\data.txt'
        self.font_file_path = r'Resources\msyh.ttc'
        self.font_title = FontProperties(fname=self.font_file_path, size=14)
        self.font_xlable = FontProperties(fname=self.font_file_path, size=10)
        self.font_ylable = FontProperties(fname=self.font_file_path, size=10)
