# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:10:21 2021

@author: Egemen G
"""

from tkinter import *
from random import randint

tk = Tk()

W,H = 400,400

r = 50




ball_coords = ((W/2)-(r/2)), r+10, ((W/2)+(r/2)), ( 2*r )+10

canvas = Canvas(tk, width=W, height=H)
canvas.pack()



ball = canvas.create_oval( ball_coords, fill='red')



Vx = 10
Vy = 10
g=50
def fall():
    global Vx, Vy, g
    print(g)
    canvas.move(ball, Vx,Vy)
    if (g<=20):
        g=10
    canvas.after(g,fall)
    
    left,top,right,bot = canvas.coords(ball)
    
    if (top<=0 or bot >=H):       
        Vy = -Vy
        g-=5
        
    if(left <=0 or right >=W):
        Vx = -Vx
        g-=5
        
        
    
     
    

fall()

tk.mainloop()
