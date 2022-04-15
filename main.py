"""
Created on Tue Nov 24 22:02:29 2020

@author: Mu-Ping
"""

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation

class Graham_scan():
    
    def __init__(self):
        self.points = []
        self.plot = []
        
    def gen_data(self):
        plt.clf()
        plt.title("Data Distribution", fontsize=28)
        plt.xlabel('x asix', fontsize=20)
        plt.ylabel('y asix', fontsize=20)
        plt.xlim(-1200, 1200)
        plt.ylim(-1200, 1200)
        
        for _ in range(points_num.get()): #群數
            center_x = np.random.randint(-600, 600)
            center_y = np.random.randint(-600, 600)
            self.points.append([center_x, center_y])
            plt.plot(center_x, center_y, 'o', ms=5 , color = 'gray', alpha=1) #畫圖 ms：折點大小
           
        canvas.draw()
        
        
    def start(self):   
        ani = animation.FuncAnimation(fig=fig, func=self.update, frames=self.frames, init_func = self.init, interval=1200, blit=False, repeat=False) #動畫
        canvas.draw()
        
    def init(self): 
        pass
    def update(self, i): #2維資料更新參數
        pass
    def frames(self): # 禎數生成器
        pass

window = tk.Tk()
window.geometry("750x650")
window.resizable(False, False)
window.title("Graham-scan Algorithm ")
window.configure(bg='#E6E6FA')

# Global var
points_num = tk.IntVar()#群
points_num.set(15)

# tk Frame
setting1 = tk.Frame(window, bg="#F0FFF0")
setting1.pack(side='top', pady=10)
setting2 = tk.Frame(window)
setting2.pack(side='top')

# Plot
fig = plt.figure(figsize=(8,8))

canvas = FigureCanvasTkAgg(fig, setting2)  # A tk.DrawingArea.
canvas.get_tk_widget().grid()

# Algorithm
brain = Graham_scan()
brain.gen_data()

# GUI
tk.Label(setting1, font=("Calibri", 15, "bold"), text="Number of points:", bg="#F0FFF0").pack(side='left', padx=5)
tk.Entry(setting1, width=5, textvariable=points_num).pack(side='left')
btn = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Generate Points', command = brain.gen_data)
btn.pack(side='left', padx=(10, 5), pady=5)
btn = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Start finding convex hull', command = brain.start)
btn.pack(side='left', padx=(5, 10), pady=5)

window.mainloop()