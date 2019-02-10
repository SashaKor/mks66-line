from display import *



def draw_line( x0, y0, x1, y1, screen, color ):
    #setting origin pt, want second set of coors to be bigger than first
    #swap procedure
    if (x0 > x1):
        originX= x0
        originY= y0
        x0= x1
        y0= y1
        x1= originX
        y1= originY

    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    C = x1-x0

    if (C == 0):
        m= 10^5 #handling case when div by zero
    else:
        m = A / C

    #draw vertical line
    if m == 10^5:
        while y <= y1:
            plot(screen, color, x, y)
            y+=1

    # octant 1
    if (m <= 1 and m >= 0 ):
        #print("octant 1 m: "+str(m))
        d = 2*A+B
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:# error counting
                y += 1
                d +=2*B
            x += 1
            d += 2*A

    # octant 2
    if (m > 1 and m != 10^5):
        #print("octant 2 m: "+ str(m))
        d= A+(2*B)
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x+= 1
                d+= 2*A
            y+= 1
            d+= 2*B

    #Octant 8;  again with the horizontal movement and vertical adjustment, but negative
    if (m < 0 and m >= -1 ):
        #print("octant 8 m: "+str(m))
        d = 2*A+B
        while x<= x1:
            plot(screen, color, x, y)
            if d > 0:# error counting
                y -= 1
                d += 2*B
            x += 1
            d -= 2*A

    #Octant 7 like octant 2 but negative
    if (m < -1 and m != 10^5):
        #print("octant 7 m: "+ str(m))
        d= A+2*B
        while y >= y1:
            plot(screen, color, x, y)
            if d < 0:
                x+=1
                d-=2*A
            y -=1
            d += 2*B
