import turtle
import time
flagWidth=600

flagHight=flagWidth*2/3

screenLocation = [flagWidth, flagHight, 300, 100]  # 定义国旗参数
starColor = [250, 244, 8]  # 定义五星颜色
flagColor = [244, 0, 2]  # 定义国旗颜色
mainStarCenter = [-screenLocation[0] / 3, screenLocation[1] / 4]  # 大五角星的中心点，在该长方形上五下五、左五右十之处
miniStarCenter1 = [-screenLocation[0] / 6, screenLocation[1] * 2 / 5]  # 上二下八、左十右五之处
miniStarCenter2 = [-screenLocation[0] / 10, screenLocation[1] * 3 / 10]  # 上四下六、左十二右三之处
miniStarCenter3 = [-screenLocation[0] / 10, screenLocation[1] * 3 / 20]  # 上七下三、左十二右三之处
miniStarCenter4 = [-screenLocation[0] / 6, screenLocation[1] * 1 / 20]  # 上九下一、左十右五之处

#定义绘制五星函数
def draw_Star(centerPoint,starR):
    assert isinstance(centerPoint, object)
    turtle.hideturtle()
    turtle.setposition(centerPoint)
    turtle.setheading(162)
    print(turtle.position())
    turtle.forward(starR)

    turtle.setheading(0)
    turtle.pendown()  # 落笔，开始绘制
    turtle.begin_fill()
    turtle.fillcolor(starColor)
    for i in range(5):
        turtle.forward(starR*1.9)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
drawStartTime=time.perf_counter()  #开始计时
# 绘制国旗窗体
turtle.colormode(255)  # 改变GRB模式为255制
turtle.setup(screenLocation[0], screenLocation[1], screenLocation[2], screenLocation[3])  # 宽度、高度、相对屏幕左上角X坐标，相对屏幕左上角Y坐标
turtle.bgcolor(flagColor)
turtle.title("绘制中国国旗")
turtle.penup()  # 画笔抬起

#画星准备
turtle.pensize(1)  # 设置画笔宽度 别名width
turtle.pencolor(starColor)  # 颜色名称，或者RGB数值

draw_Star(mainStarCenter,screenLocation[0] * 3 / 20) # 画大五星
draw_Star(miniStarCenter1,screenLocation[0] / 20) # 画第一颗小五星
draw_Star(miniStarCenter2,screenLocation[0] / 20) # 画第二颗小五星
draw_Star(miniStarCenter3,screenLocation[0] / 20) # 画第三颗小五星
draw_Star(miniStarCenter4,screenLocation[0] / 20) # 画第四颗小五星

drawEndTime=time.perf_counter()  #结束计时
print(str(drawEndTime-drawStartTime))
turtle.done()

