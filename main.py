"""
Created on Tue Nov 24 22:02:29 2020

@author: Mu-Ping
"""

import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation

class Graham_scan():
    
    def __init__(self):
        self.points = []
        self.plot = []
        
    def gen_data(self):
        plt.clf()
        plt.title("Data")
        plt.xlim(-1200, 1200)
        plt.ylim(-1200, 1200)
        
        data=[]
        for _ in range(points_num.get()): #群數
            center_x = np.random.randint(-700, 700)
            center_y = np.random.randint(-700, 700)
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
window.geometry("600x650")
window.resizable(False, False)
window.title("Graham-scan Algorithm ")

# Global var
points_num = tk.IntVar()#群
points_num.set(15)
color = ["#FF0000", "#0000E3", "#FFD306", "#F75000", "#02DF82", "#6F00D2", "#73BF00"]

# tk Frame
setting1 = tk.Frame(window)
setting1.pack(side='top', pady=10)
setting2 = tk.Frame(window)
setting2.pack(side='top')

# Plot
fig = plt.figure(figsize=(8,8))
plt.title("Data Distribution", fontsize=20)
canvas = FigureCanvasTkAgg(fig, setting2)  # A tk.DrawingArea.
canvas.get_tk_widget().grid()

# Algorithm
brain = Graham_scan()
brain.gen_data()

# GUI
tk.Label(setting1, font=("Calibri", 12, "bold"), text="Points:").grid(row=0, column=0, padx=5)
tk.Entry(setting1, width=5, textvariable=points_num).grid(row=0, column=1)
btn = tk.Button(setting1, font=("Calibri", 10, "bold"), text='Generate', command = brain.gen_data)
btn.grid(row=0, column=2, padx=20)
btn = tk.Button(setting1, font=("Calibri", 10, "bold"), text='Start', command = brain.start)
btn.grid(row=0, column=3)

window.mainloop()

