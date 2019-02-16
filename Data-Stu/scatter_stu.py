import matplotlib.pyplot as plt
input_values = list(range(1, 1001))
output_values = [x**2 for x in input_values]
plt.scatter(input_values, output_values, c=input_values, cmap=plt.cm.Reds, s=10)
plt.title("Scatter", fontsize=24)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Output Value",fontsize=14)  #y轴坐标
plt.axis([0,1100,0,1100000])  # 指定坐标轴取值范围
plt.tick_params(axis='both',which='major', labelsize =10)  # 坐标轴字体
plt.grid(True)
plt.show()