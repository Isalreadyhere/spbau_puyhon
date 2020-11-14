import turtle as tl

def draw_fractal(size):
    if size >= 8:
        tl.pensize(min(5, max(size / 20, 2)))
        tl.forward(size)
        tl.left(90)
        tl.forward(size)
        tl.left(90)
        draw_fractal(size/2)
        tl.pensize(min(5, max(size / 20, 2)))
        tl.forward(size)
        tl.left(90)
        tl.forward(size)
        tl.left(90)
        draw_fractal(size/2)
        tl.pensize(min(5, max(size / 20, 2)))
        tl.forward(size/2)
        
        draw_fractal(size/4)
        tl.backward(size/2)

        tl.left(90)
        tl.forward(size/2)
        tl.right(90)
        draw_fractal(size/4)
        tl.left(90)
        tl.backward(size/2)
        tl.right(90) 

       
    #else:
         #tl.pensize(3)
         #tl.dot()
        
size = 550
tl.speed(0)
tl.delay(-1)  # уменьшение задержки для скорости
tl.penup()
tl.color('green')
tl.goto(0, -size/1.5 - 20)
tl.setheading(45)
tl.pendown()

draw_fractal(size)
tl.done()