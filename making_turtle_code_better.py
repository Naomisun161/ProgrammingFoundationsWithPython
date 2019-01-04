import turtle

paper = turtle.Screen() # set up a paper to draw
paper.bgcolor("red")

def draw_square():
    lu = turtle.Turtle() # init a turtle named lu
    lu.color("yellow")
    lu.show("turtle")
    for i in range(0,4):
        lu.forward(100)
        lu.right(90)
               
def draw_circle():
    site = turtle.Turtle() # init a turtle named site
    site.color("yellow")
    site.shape("turtle")
    site,circle(100)

def draw_triangle():
    tim = turtle.Turtle() # init a tirtle named tim
    tim.color("yellow")
    tim.shape("turtle")
    for i in range(0,3):
        tim.forward(100)
        tim.left(120)

draw_square()
draw_circle()
draw_triangle()
    
