import turtle
import time
turtle.colormode(255)  # 改变GRB模式为255制
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):  #划线函数
    drawGap()
    turtle.pencolor(123,104,238)
    if draw:
        turtle.pendown()
    else :
        turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    for i in date:
        drawDigit(eval(i))
def drawDataWithYMD(date):
    for i in date:
        if i=='Y':
            turtle.pencolor("green")
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i=='M':
            turtle.pencolor("green")
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i=='D':
            turtle.pencolor("green")
            turtle.write('日',font=("Arial",18,"normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.hideturtle()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDataWithYMD(time.strftime('%YY%mM%dD',time.gmtime()))
    turtle.done()
main()