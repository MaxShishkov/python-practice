import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(10)

    brad.pu()
    brad.setpos(200,0)
    brad.pd()

    # draw circle using squares
    for n in xrange(36):
        for i in xrange(4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    turtle.hideturtle()

    brad.pu()
    brad.setpos(-200,0)
    brad.pd()

    #draw flower
    
    for i in xrange(36):
        brad.left(35)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(145)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(10)

    brad.right(90)
    brad.forward(300)

    #add leaf
    brad.right(180)
    brad.forward(100)
    brad.right(45)

    brad.left(35)
    brad.forward(65)
    brad.right(35)
    brad.forward(65)
    brad.right(145)
    brad.forward(65)
    brad.right(35)
    brad.forward(65)
    
    window.exitonclick()

draw_shape()
