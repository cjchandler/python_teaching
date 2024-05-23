import turtle
import time
turtle.color('red', 'yellow')
turtle.begin_fill()

def square_func():
    turtle.forward(100)
    turtle.right(90)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(100)
    turtle.right(90)
    return

def ngon_func( n , r ):
    deg_for_corner = 360/n
    l = r*2*3.14/n
    
    for a in range( 0 , n):
        turtle.forward(l)
        turtle.right(deg_for_corner)
    
    return

def basic_window( size ):
    turtle.forward(size)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(size)
    return

def window( height, width ):
    turtle.forward(width)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(width)
    return

def print_today_date():
    return ( "jun 9 2023") 

def add( a , b ) :
    y = a + b 
    return y 


##THIS IS WHERE THE CODE REALY STARTS

ngon_func( 15 , 200 )
    # ~ basic_window(200)
    # ~ basic_window(100)
    # ~ basic_window(50)
    # ~ basic_window(25)

    
turtle.done()    



# ~ color('red', 'yellow')
# ~ begin_fill()
# ~ while True:
    # ~ forward(200)
    # ~ left(170)
    # ~ if abs(pos()) < 1:
        # ~ break
# ~ end_fill()
# ~ done()
