from gui_files.svg import *
import math
import random
from PIL import Image
import numpy as np

DICE_CAPTION = "xlb piggies (the pips change--can you spot them all?)"
def rgbtohex(r,g,b):
    return "#" + hex(r//16)[2:] + hex(r%16)[2:] + hex(g//16)[2:] + hex(g%16)[2:]+ hex(b//16)[2:]+hex(b%16)[2:]
def draw_eyes1(graphic, x, y, r):
    draw_circle(graphic, x+r/4, y-r/4, 2)
    draw_circle(graphic, x-r/4, y-r/4, 2)

    draw_circle(graphic, x+r/4, y-r/3, 0.25, stroke="white", fill="white")
    draw_circle(graphic, x-r/4, y-r/3, 0.25, stroke="white", fill="white")

def draw_eyes2(graphic, x, y, r):
    draw_line(graphic,x+r/4-1.5, y-r/4, x+r/4+1.5, y-r/4)
    draw_line(graphic,x-r/4-1.5, y-r/4, x-r/4+1.5, y-r/4)

def piggy_base(graphic, x,y,r,c):
    #ears
    draw_triangle(graphic, x-r, y, x-r, y-r, x, y-r, stroke="#913c24", fill="#e3b9b6")
    draw_triangle(graphic, x+r, y, x+r, y-r, x, y-r, stroke="#913c24", fill="#e3b9b6")

    #pig
    draw_circle(graphic, x, y, r, stroke="#913c24", fill="#e3b9b6")

    #nose circle
    draw_circle(graphic, x, y + r/3, r*0.5, stroke="#b0715f", fill=c)

    #nose
    draw_circle(graphic, x + r/4, y + r/4, 1, stroke="#b0715f", fill="#b0715f")
    draw_circle(graphic, x - r/4, y + r/4, 1, stroke="#b0715f", fill="#b0715f")

def draw_piggy(graphic, x,y,r):
    rannum = random.randint(1,7)
    filename = "p" + str(rannum) + ".png"

    im = Image.open(filename)
    # imarr = list(im.getdata())
    imarr = np.array(im)

    for i in range(len(imarr[0])):
        for j in range(len(imarr)): #i, j are locations
            temp = imarr[j][i]
            color = rgbtohex(temp[0], temp[1], temp[2])
            draw_rect(graphic, i+x-16, j+y-16, 1, 1, stroke=color, fill=color)
    # if rannum==1:
    #     piggy_base(graphic, x, y, r, "#e3b9b6")
    #     draw_eyes1(graphic, x, y, r)
    # elif rannum==2:
    #     piggy_base(graphic, x, y, r, "#e3b9b6")
    #     draw_eyes2(graphic, x, y, r)
    # else:
    #     piggy_base(graphic, x, y, r, "#e3b9b6")

def draw_background(graphic, filename):
    im = Image.open(filename)
    # imarr = list(im.getdata())
    imarr = np.array(im)[...,:3]

    for i in range(len(imarr[0])):
        for j in range(len(imarr)): #i, j are locations
            temp = imarr[j][i]
            color = rgbtohex(temp[0], temp[1], temp[2])
            draw_rect(graphic, i, j, 1, 1, stroke=color, fill=color)

def draw_dice(num):
    # **YOUR CODE HERE**
    width, height = 100, 100
    graphic = create_graphic(width, height)
    if num == 1:
        draw_background(graphic, "1.png")
        return graphic
    elif num ==6:
        draw_background(graphic, "6.png")
        return graphic
   # draw_rect(graphic, 0, 0, 100, 100, fill="(211, 149, 222, 255)", stroke="(211, 149, 222, 255)")
    draw_background(graphic, "bg.png")
    rows = max(2, num//2) if num%2 == 0 else math.ceil(num/2)

    for i in range(1,rows+1): #draw the pips
        if num <= 0:
            break #done
        #look @ the number of rows
        y = height * i/(rows+1)
        if num %2 == 1 and num <= 3 : #only draw one
            x = width/2
            draw_piggy(graphic, x, y, 15)
            num-=1
        else:
            for j in range(1, 3):
                x = width*j/(3)
                draw_piggy(graphic, x, y, 15)
                num -= 1
    return graphic
