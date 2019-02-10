from display import *
from draw import *

screen = new_screen()

color = [ 255, 0, 0 ]
color1 = [ 0, 0, 255 ]

'''
Gallery Pic Code
'''
'''
def drawTri(x0,y0,x1,y1,x2,y2,screen,color):
    draw_line(x0,y0,x1,y1,screen,color)
    draw_line(x1,y1,x2,y2,screen,color)
    draw_line(x2,y2,x0,y0,screen,color)

def drawCool(x0,y0,screen,color):
    x1=x0+50
    y1=y0+200
    x2=x0-50
    y2=x0+200
    for i in range(500):
        drawTri(x0,y0,x1,y1,x2,y2,screen,color)
        color[0]-= 10
        color[2]+= 10
        x1 += 10
        x2 -= 10

drawCool(250,100,screen,color) #omg wut is this
'''
'''
 Required test cases
'''

# undefined slope; vert line
draw_line(250,0,250,500,screen,color)
# slope == 0; horiz line
draw_line(0,250,500,250,screen,color)
#draw_line(500,250,0,250,screen,color)
# slope == 1
draw_line(0,0,500,500,screen,color)
#draw_line(500,500,0,0,screen,color) #reversed also works for all!
# slope == -1
draw_line(500,0,0,500,screen,color)
# octant 1 (slope <=1 && >= 0)
draw_line(250,250,750,500,screen,color)
# octant 2 (slope > 1 && < vert line; vert line handled as sep. case)
draw_line(250,250,450,550,screen,color)
# octant 3 (same process as for 7)
draw_line(250,250,50,550,screen,color)
# octant 4 (same process as for 8)
draw_line(250,250,-150,450,screen,color)
# octant 5 (same process as for 1)
draw_line(-250,0,250,250,screen,color)
# octant 6 (same process as for 2)
draw_line(-150,-350,250,250,screen,color)
# octant 7 (slope < -1 && < vert line)
draw_line(250,250,450,-50,screen,color)
# octant 8 (slope < 0 && >= -1)
draw_line(250,250,1250,-250,screen,color)

display(screen)
save_extension(screen, 'img.png')
