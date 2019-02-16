# 导入库
import re
import numpy
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
from data_settings import Settings

figure_settings = Settings()
'''数据读取'''
with open(figure_settings.data_file_path, 'r') as data_object:
    all_data = data_object.readlines()

'''数据处理'''
costs = []
sales = []
for single_data in all_data:
    tmp_data = re.split('\t|\n', single_data)
    costs.append(float(tmp_data[0]))
    sales.append(float(tmp_data[1]))

costs = numpy.array(costs).reshape([-1, 1])  # 由列表类型转换为数组类型
sales = numpy.array(sales).reshape([-1, 1])  # 由列表类型转换为数组类型

'''数据展示'''
plt.scatter(costs, sales, c=costs,s=20)
plt.title("销售费用与销售金额关系", fontproperties=figure_settings.font_title)
plt.xlabel("销售费用", fontproperties=figure_settings.font_xlable)
plt.ylabel("销售金额", fontproperties=figure_settings.font_ylable)
plt.axis([0,60000,0,150000])  # 指定坐标轴取值范围
plt.tick_params(axis='both',labelsize=10)
plt.grid(True)
plt.show()

'''数据建模'''
figuare_linear_model = lm.LinearRegression()
figuare_linear_model.fit(costs,sales)

'''模型评估'''
model_coef = figuare_linear_model.coef_  # 回归系数
model_intercept = figuare_linear_model.intercept_  #截距
r2 = figuare_linear_model.score(costs, sales)  #决定系数
print(model_coef)

'''销售预测'''
new_x = 84610
new_x=numpy.array(new_x).reshape([-1, 1])
pre_y = figuare_linear_model.predict(new_x)
print(pre_y)