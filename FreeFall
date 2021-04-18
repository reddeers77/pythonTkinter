# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 21:10:45 2021

@author: Egemen G
"""


from tkinter import *
from random import randint
from math import sqrt

tk = Tk()

W,H = 300,800

dia = 20




ball_coords = ((W/2)-(dia/2)), 0, ((W/2)+(dia/2)), ( dia )

canvas = Canvas(tk, width=W, height=H)
canvas.pack()


ball = canvas.create_oval( ball_coords, fill='red')



g = 9.8
h = H/100
h1 = (h-(dia/2)/100)

velocity = 0


def fall():
    
    global  g, potential, velocity, h1 
    
    
    left,top,right,bot = canvas.coords(ball)
    
    kinetic1 = (velocity**2)/2
    potential1 = (g*h1)
    print(kinetic1)
    canvas.move(ball, 0, velocity)
    # 1 sn = 1000 ms
    canvas.after(100, fall)
    
    if velocity == 0:
        potential2 = g*(h1-1)
        kinetic2 = potential1-potential2-kinetic1
        velocity = sqrt(2*(potential1+kinetic1-potential2))
        h1 = h1-1
        
        
    else:
        
        h2  = h1-top-(dia/200)
        potential2 = g*h2
        kinetic2 = potential1+kinetic1-potential2
        velocity = sqrt(2*(potential1+kinetic1-potential2))
        h1 =h2
        
    if (top>10000):
        sys.exit()
    
    
fall()

tk.mainloop()
