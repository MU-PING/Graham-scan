"""
Created on Tue Nov 24 22:02:29 2020

@author: Mu-Ping
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

from tkinter import ttk 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation

class PointNode():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def setDegree(self, degree):
        self.degree = degree
        
class Graham_scan():
    
    def __init__(self):
        self.startpoint = None
        self.points = []  # all pooints except startpoint
        
    def gen_data(self):
        
        # set plot
        plt.clf()
        plt.title("Data Distribution", fontsize=28)
        plt.xlabel('x asix', fontsize=20)
        plt.ylabel('y asix', fontsize=20)
        plt.xlim(-1200, 1200)
        plt.ylim(-1200, 1200)
        
        # generate points--------------------------------------------
        tempPoints = []
        tempY = 600
        
        for _ in range(points_num.get()): # number of points
            centerX = np.random.randint(-1000, 1000)
            centerY = np.random.randint(-1000, 1000)
            point = PointNode(centerX, centerY)
            
            if centerY <= tempY:
                tempY = centerY
                self.startpoint = point
                
            tempPoints.append(point)   
        tempPoints.remove(self.startpoint)    
        
        # count degree and sort by angle------------------------
        for point in tempPoints:
            degree = math.degrees(math.atan2(point.y - self.startpoint.y, point.x - self.startpoint.x))
            point.setDegree(degree)
        
        self.points = sorted(tempPoints, key = lambda point: point.degree)
        self.points.insert(0, self.startpoint)
        
        # make plot--------------------------------------------
        for index in range(len(self.points)):
            point = self.points[index]
            plt.plot(point.x, point.y, 'o', ms=5 , color = '#1f77b4', alpha=1) # ms: point size        
            plt.text(point.x+35, point.y-20, str(index+1))
        canvas.draw()
        
        
    def start(self):   
        ani = animation.FuncAnimation(fig=fig, func=self.update, frames=self.frames, init_func = self.init, interval=1200, blit=False, repeat=False) #動畫
        canvas.draw()
        
    def init(self): 
        pass
 
        
    def update(self, i):
        pass
    
    def frames(self):
        pass

window = tk.Tk()
window.geometry("750x650")
window.resizable(False, False)
window.title("Graham-scan Algorithm ")
window.configure(bg='#E6E6FA')

# Global var
points_num = tk.IntVar()
points_num.set(15)

# tk Frame
setting1 = tk.Frame(window, bg="#F0FFF0")
setting1.pack(side='top', pady=10)
separator = ttk.Separator(window, orient='horizontal')
separator.pack(side='top', fill=tk.X)
setting2 = tk.Frame(window)
setting2.pack(side='top', pady=10)

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
btn = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Generate points', command = brain.gen_data)
btn.pack(side='left', padx=(10, 5), pady=5)
btn = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Start finding convex hull', command = brain.start)
btn.pack(side='left', padx=(5, 10), pady=5)

window.mainloop()