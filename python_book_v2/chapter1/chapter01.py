# @时间 : 2019-8-14 13:36 
# @作者 : 孙会想
# @文件 : chapter01.py 
# @工具: PyCharm

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

raw_data = pd.read_csv('data.txt')

num = int(raw_data.shape[0]*0.7)
x,y = raw_data[['money']],raw_data[['amount']]
x_train,x_test = x[:num],x[num:]
y_train,y_test = y[:num],y[num:]

plt.scatter(x_train, y_train)
plt.show()

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

predict_test_y = model.predict(x_test)
print("Mean squared error: %.0f"
      % mean_squared_error(y_test, predict_test_y))
print('Variance score: %.2f' % r2_score(y_test, predict_test_y))

model_coef = model.coef_
model_intercept = model.intercept_
print('coef is: ',model_coef)
print('intercept is: ',model_intercept)

x_new = 84619
print(x_new)
x_new = np.array(x_new).reshape(1, -1)
y_pre = model.predict(x_new)
print(y_pre)