import matplotlib.pyplot as plt

input_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
output_values = [1, 4, 9, 16, 25, 60, 23, 67, 88, 88, 66, 34]
plt.plot(input_values, output_values, linewidth = 5)  #  绘制折线图
plt.title("Output Value",fontsize = 24)
plt.xlabel("Month",fontsize = 12)
plt.ylabel("Output Value",fontsize = 14)  #y轴坐标
plt.tick_params(axis='both',labelsize =10)  # 坐标轴字体
plt.grid(True)
plt.show()