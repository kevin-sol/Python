import turtle
# 海龟初始化
pen = turtle.Pen()
turtle.bgcolor("black") # 背景颜色
turtle.title("烟花")
pen.speed(100)

for x in range(180):
    step = 300

    if x % 2 == 0:
        pen.color("red")
        step = 300
    elif x % 3 ==0:
        pen.color("green")
        step = 250
    elif x % 5 == 0:
        pen.color("yellow")
        step = 150
    else:
        pen.color("pink")
        step = 100

    pen.forward(step)# 按照步长画直线
    pen.dot(6)
    pen.backward(step)# 原路返回
    pen.right(2)# 每次循环向右转2度

turtle.done()