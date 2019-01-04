import turtle
def draw_square():
    paper = turtle.Screen() # provide a window to show my graph
    
    paper.bgcolor("red") # set up the paper 
    
    brad = turtle.Turtle() # set up brad
    brad.color("yellow")
    brad.shap("turtle")
    brad.speed(2)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    
    paper.exitonclick()
