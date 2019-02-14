# -*- coding: utf-8 -*-

import time
import random
from tkinter import messagebox
import tkinter as tk

#小球初位置，BlueBall 86像素长宽
x =random.randint(43,757)
y =random.randint(67,257)
#RedBase初位置，base 23像素宽，227像素长
x2 =400.0
y2 =11.5
#GreenBase初位置，base 23像素宽，227像素长
x3 = 400.0
y3 = 588.5


vx =1.0#是ball的速度
vy =3.0
vx20 =0.8#2是电脑RedBase的速度

x_min =43.0#球的运动范围
y_min =66.0
x_max =757.0
y_max =534.0
x2_min =113.5#板的运动范围
x2_max =686.5

sleep_time =0.005

root =tk.Tk()
root.title('Boucing Ball!')
#root.geometry('800x600')

#左右按键
def goLeft():
    global x3
    new_x3 = x3 - 20.0
    if new_x3 < x2_min:
        new_x3 = x3
    x3 = new_x3

def goRight():
    global x3
    new_x3 = x3 + 20.0
    if new_x3 > x2_max:
        new_x3 = x3
    x3 = new_x3
    
#菜单
menubar=tk.Menu(root)

Homemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Home',menu=Homemenu)
Homemenu.add_command(label='New',command = goLeft)
Homemenu.add_command(label='Stop',command = goLeft)
Homemenu.add_command(label='Save',command=goLeft)
Homemenu.add_separator()
Homemenu.add_command(label='Exit',command=root.quit)

Settingmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Setting',menu=Settingmenu)
submenu=tk.Menu(Settingmenu)
Settingmenu.add_cascade(label='难度选择',menu=submenu,underline=0)
submenu.add_command(label='贼简单',command=goLeft)
submenu.add_command(label='一般简单',command=goLeft)
submenu.add_command(label='挺难的',command=goLeft)

root.config(menu=menubar)


#画布
frame1 = tk.Frame(height = 600,width = 800)
frame2 = tk.Frame(height = 600,width = 30)

frame3 = tk.Frame(frame2,height = 30,width = 400)
frame4 = tk.Frame(frame2,height = 30,width = 400)

frame1.grid(row = 0,column = 0)
frame2.grid(row = 1,column = 0)

frame3.pack(side = 'left')
frame4.pack(side = 'right')

canvas = tk.Canvas(frame1,width=800, height=600,bg='white')
canvas.grid()
#按键
left = tk.Button(frame3,text = 'Left',command = goLeft)
left.pack()
right = tk.Button(frame4,text = 'Right',command = goRight)
right.pack()

Ball = tk.PhotoImage(file = 'BlueBall.png')
width1 = Ball.width()
height1 = Ball.height()
image_x =(width1)/2.0
image_y =(height1)/2.0

RedBase = tk.PhotoImage(file = 'RedBase.png')
width2 = RedBase.width()
height2 = RedBase.height()
image_x =(width2)/2.0
image_y =(height2)/2.0

GreenBase = tk.PhotoImage(file = 'GreenBase.png')
width3 = GreenBase.width()
height3 = GreenBase.height()
image_x =(width3)/2.0
image_y =(height3)/2.0

#判定游戏结束的函数
def judge():
    #如果电脑一边碰壁，游戏结束
    if  y == y_min:
        if x <= (x2 -11.5)  or x >= (x2 + 11.5):
            messagebox.showwarning(title='Hey!', message='You win!')
            return False
        else:
            return True
    #如果玩家一边碰壁，游戏结束
    if y == y_max:
        if x <= (x3 - 11.5) or x >= (x3 + 11.5): 
            messagebox.showwarning(title='Hey!', message='You lose!')
            return False
        else:
            return True
    #如果按暂停，跳回循环前
    #if
    else:
        return True
    
while judge():
    new_x = x+ vx#小球运动方程
    x = new_x
    new_y = y+ vy
    y = new_y
    if new_x >= x_max or new_x <= x_min:
        vx = vx*-1.0
    if new_y >= y_max or new_y <= y_min:
        vy = vy*-1.0
        
    if x > x2:#电脑板板运动方程
        vx2 = vx20
    else:
        vx2 = vx20 * -1.0
    new_x2 = x2+ vx2
    if new_x2 >= x2_max or new_x2 <= x2_min:
        new_x2 = x2
    x2 = new_x2
    
    canvas.create_image(x, y, image = Ball,tag ="Ball")
    canvas.create_image(x2, y2, image = RedBase,tag ="RedBase")
    canvas.create_image(x3, y3, image = GreenBase,tag ="GreenBase")
    canvas.update()
    time.sleep(sleep_time)
    canvas.delete("Ball")
    canvas.delete("RedBase")
    canvas.delete("GreenBase")

root.mainloop()
    


