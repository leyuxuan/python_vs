#ClickAndSmile.py
import turtle
t = turtle.Pen()
t.speed(0)
t.hideturtle()
t.width(1/2)
turtle.bgcolor("black")
def draw_smiley(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # Face
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50/2)
    t.end_fill()
    # Left eye
    t.setpos(x-15/2, y+60/2)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10/2)
    t.end_fill()
    # Right eye
    t.setpos(x+15/2, y+60/2)
    t.begin_fill()
    t.circle(10/2)
    t.end_fill()
    # Mouth
    t.setpos(x-25/2, y+40/2)
    t.pencolor("black")
    t.width(10/2)
    t.goto(x-10/2, y+20/2)
    t.goto(x+10/2, y+20/2)
    t.goto(x+25/2, y+40/2)
    t.width(1/2)
turtle.onscreenclick(draw_smiley)


