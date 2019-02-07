from display import *



def draw_line( x0, y0, x1, y1, screen, color ):
    #setting origin pt
    x = x0
    y = y0
    A= y1-y0
    B= -(x1-x0)

    if(0 == B):
        m= 10^8
    else:
        m= A/B
    print(m)
    #octant 1
    if (m <= 1 and m >= 0 ):
        print("here")
        d= 2*A+B
        while x<= x1:
            plot(screen, color, x, y)
            if d > 0:# error counting
                y += 1
                d+=2*B
            x += 1
            d += 2*A

    '''
    # octant 2 setup
    x = x0
    y = y0
    A= y1-y0
    B= -(x1-x0)
    preserved from before
    '''
    if (m <= 1 and m >= 0 ):
        d= A+2*B
        while y<= y1:
            plot(screen, color, x, y)
            if d > 0:
                x+=1
                d+=2*A
            y+=1
            d+= 2*B

    if (m <= 1 and m >= 0 ):
        d= A+2*B
        while y<= y1:
            plot(screen, color, x, y)
            if d > 0:
                x+=1
                d+=2*A
            y+=1
            d+= 2*B
