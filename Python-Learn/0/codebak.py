#pythonDraw bak
import turtle  # 引入海龟库
from typing import List

screenLocation: List[int]=[1000,550,480,300]  #定义海归画布参数
penColor: List[int]=[212,222,2] #定义画笔颜色

turtle.setup(screenLocation[0], screenLocation[1],screenLocation[2],screenLocation[3])  # 宽度、高度、相对屏幕左上角X坐标，相对屏幕左上角Y坐标
turtle.penup()  # 画笔抬起
turtle.forward(-450)
turtle.pendown()  # 落笔，开始绘制
turtle.pensize(15)  # 设置画笔宽度 别名width
turtle.colormode(255)  # 改变GRB模式为255制
turtle.pencolor(penColor)  # 颜色名称，或者RGB数值
turtle.setheading(-40)  # 改变爬行角度  为绝对角度别名seth
for i in range(5): #循环4次  如果是M,N则是从产生从M,到N-1个数值
    turtle.circle(50, 90)  #根据半径r绘制extent角度的弧形  正数为海龟左侧半径r处为原点，负数为海龟右侧半径r为原点；如果有角度参数则右转参数角度，默认360度。
    turtle.circle(-40, 90)
turtle.circle(40, 80 / 2)
turtle.forward(40)  # 前进  别名fd  如果是负数，则为倒退
turtle.circle(16, 180)
turtle.forward(40 * 2 / 3)
turtle.done()  #完成后窗体不退出



#以下是画五星
turtle.forward(-450)
turtle.pendown()  # 落笔，开始绘制
turtle.pensize(10)  # 设置画笔宽度 别名width
turtle.pencolor(starColor)  # 颜色名称，或者RGB数值

for i in range(5):
    turtle.forward(300)
    turtle.right(144)

turtle.done()

# 画辅助线
turtle.pensize(1)
turtle.pencolor(sublineColor)
turtle.backward(screenLocation[0] / 2)  # 回退到国旗边缘

turtle.pendown()
turtle.forward(screenLocation[0])
turtle.penup()

turtle.left(90)
turtle.forward(screenLocation[1] / 2)
turtle.left(90)
turtle.forward(screenLocation[0] / 2)
turtle.left(90)
turtle.pendown()
turtle.forward(screenLocation[1])
turtle.penup()

turtle.setposition(mainStarCenter)
turtle.setheading(162)
print(turtle.position())
turtle.forward(screenLocation[0] * 3 / 20)

turtle.setposition(mainStarCenter)
turtle.setheading(162)
print(turtle.position())
turtle.forward(screenLocation[0] * 3 / 20)

turtle.setheading(0)
turtle.pendown()  # 落笔，开始绘制
turtle.begin_fill()
turtle.fillcolor(starColor)
for i in range(5):
    turtle.forward(screenLocation[0] * 5.7 / 20)
    turtle.right(144)
turtle.end_fill()
turtle.penup()

# 第一颗小星
turtle.setposition(miniStarCenter1,screenLocation[0] / 20)
turtle.setheading(162)
print(turtle.position())
turtle.forward(screenLocation[0] / 20)

turtle.setheading(0)
turtle.pendown()  # 落笔，开始绘制
for i in range(5):
    turtle.forward(screenLocation[0] * 1.9/ 20)
    turtle.right(144)
turtle.penup()

# 第二颗小星
turtle.setposition(miniStarCenter2)
turtle.setheading(162)
print(turtle.position())
turtle.forward(screenLocation[0] / 20)

turtle.setheading(0)
turtle.pendown()  # 落笔，开始绘制
for i in range(5):
    turtle.forward(screenLocation[0] * 1.9/ 20)
    turtle.right(144)
turtle.penup()

# 第三颗小星
turtle.setposition(miniStarCenter3)
turtle.setheading(162)
print(turtle.position())
turtle.forward(screenLocation[0] / 20)

turtle.setheading(0)
turtle.pendown()  # 落笔，开始绘制
for i in range(5):
    turtle.forward(screenLocation[0] * 1.9/ 20)
    turtle.right(144)
turtle.penup()

# 第四颗小星
turtle.setposition(miniStarCenter4)
turtle.setheading(162)
print(turtle.position())
turtle.forward(screenLocation[0] / 20)

turtle.setheading(0)
turtle.pendown()  # 落笔，开始绘制
for i in range(5):
    turtle.forward(screenLocation[0] * 1.9/ 20)
    turtle.right(144)
turtle.penup()

def charPyramid(chars,charsNum):
    for i in range(charsNum):
        tierChar="{0:*^"+str(i+1)+"}"
        print(tierChar.format(chars))


