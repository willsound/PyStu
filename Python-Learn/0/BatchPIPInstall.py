import os
# numpy 表达N维数组的最基础库
# Pandas 数据分析高层次应用库,提供了简单易用的数据结构和数据分析工具
# SciPy 数学、科学和工程计算功能库
# Matplotlib 二维数据可视化matplotib.pyplot子库  Matplotlib
# seaborn:统计类数据可视化功能库
#Mayavi:三维科学数据可视化功能库
#apriori,orange
#PyPDF2 用来处理pdf文件的工具集
#NLTK：自然语言文本处理第三方库
#Python-docx 创建或更新WORD文件的第三方库

#Scikit-learn:机器学习方法工具集
#TensorFlow  AlphaGo背后的机器学习计算框架
#MXNet  基于神经网络的深度学习计算框架

#Requests 最友好的网络爬虫功能库"mayavi",
#Scrapy  优秀的网络爬虫框架

#Web框架  Django  Pyramid Flask
libs={"numpy","Pandas","SciPy","Matplotlib","seaborn","apriori","orange","pillow","sklearn","requests","jieba","beautifulsoup4","wheel","networkx","sympy",\
      "pyinstaller","django","flask","werobot","pyqt5","pandas","pyopengl","pypef2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install"+ lib)
    print("successful")
except:
    print("Failed")