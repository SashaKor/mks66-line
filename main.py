from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
'''
draw_line(0,0,100,100,screen,color)
draw_line(100,100,200,200,screen,color)
draw_line(0,0,200,0,screen,color)
draw_line(0,0,0,200,screen,color)
draw_line(0,0,5,100,screen,color)
'''
draw_line(50,40,80,20,screen,color)
display(screen)
save_extension(screen, 'img.png')
