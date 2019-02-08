from display import *
from draw import *

screen = new_screen()

color = [ 0, 255, 0 ]


def drawRect(color):
    #
    pass

def drawTri(x0,y0,x1,y1,x2,y2,screen,color):
    #start at vert
    print("lol")
    draw_line(x0,y0,x1,y1,screen,color)
    draw_line(x1,y1,x2,y2,screen,color)
    draw_line(x2,y2,x0,y0,screen,color)

def drawCircle():
    pass

#drawTri(1,1,200,200,35,80,screen,color)
#draw_line(1,1,200,200,screen,color)
#draw_line(200,200,35,80,screen,color)
draw_line(1,1,35,80,screen,color)
draw_line(35,80,1,1,screen,color)
'''
draw_line(0,0,100,100,screen,color)
draw_line(100,100,200,200,screen,color)
draw_line(0,0,200,0,screen,color)
draw_line(0,0,0,200,screen,color)
draw_line(0,0,5,100,screen,color)
draw_line(50,40,80,20,screen,color)
draw_line(50,40,80,100,screen,color)
draw_line(0,0,0,100,screen,color)
'''

display(screen)
save_extension(screen, 'img.png')
