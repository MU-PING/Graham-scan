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
        self.degree = None
        self.plot = None
        
    def setDegree(self, degree):
        self.degree = degree
        
    def setPlot(self, plot):
        self.plot = plot
        
    def beSelected(self):
        self.plot.set_color("#ff7f0e")
        
    def beProcessed(self):
        self.plot.set_color("#d62728")
            
class Graham_scan():
    
    def __init__(self):
        self.firstPoint = None
        self.points = []
        self.points_stack = [] 
        self.segment_stack = [] 
        self.vector_stack = []  
        self.ani =None
        
    def clearPoints(self):
        self.points.clear()

    def clearStructure(self):
        self.points_stack.clear()
        self.segment_stack.clear()
        self.vector_stack.clear()
        
    def clearPlot(self):
        plt.clf()
        plt.title("Data Distribution", fontsize=28)
        plt.xlabel('x asix', fontsize=20)
        plt.ylabel('y asix', fontsize=20)
        plt.xlim(-1200, 1200)
        plt.ylim(-1200, 1200)
            
    def gen_data(self):
        
        self.clearPoints()
        self.clearPlot()
        
        # generate points--------------------------------------------
        tempY = 600
        for _ in range(points_num.get()): # number of points
            centerX = np.random.randint(-1000, 1000)
            centerY = np.random.randint(-1000, 1000)
            point = PointNode(centerX, centerY)
            point.setPlot(plt.plot(point.x, point.y, 'o', ms=5 , color = '#1f77b4', alpha=1)[0]) # ms: point size   
            
            if centerY <= tempY:
                tempY = centerY
                self.firstPoint = point
                
            self.points.append(point)   
            
        canvas.draw()
        
    def start(self):   
        self.ani = animation.FuncAnimation(fig=fig, func=self.update, frames=self.frames, init_func = self.init, interval=1200, blit=False, repeat=False) #動畫
        canvas.draw()
        
    def init(self): 

        # calculate degree and sort by degree------------------------
        self.points.remove(self.firstPoint)  
        
        for point in self.points:
            degree = math.degrees(math.atan2(point.y - self.firstPoint.y, point.x - self.firstPoint.x))
            point.setDegree(degree)
        
        self.points = sorted(self.points, key = lambda point: point.degree)
        
        # label points order--------------------------------------------
        plt.text(self.firstPoint.x+35, self.firstPoint.y-25, "1")
        for index in range(points_num.get()-1):
            point = self.points[index]
            plt.text(point.x+35, point.y-25, str(index+2))

        self.points.append(self.firstPoint)  
        
        # init stack--------------------------------------------
        secondPoint = self.points[0]
        self.firstPoint.beSelected()
        secondPoint.beSelected()
        self.points_stack.append(self.firstPoint)
        self.points_stack.append(secondPoint)
        self.segment_stack.append(plt.plot([self.firstPoint.x, secondPoint.x], [self.firstPoint.y, secondPoint.y], color = '#ff7f0e', alpha=1, linestyle="solid")[0])
        self.vector_stack.append(np.array([secondPoint.x - self.firstPoint.x, secondPoint.y - self.firstPoint.y]))
        
        canvas.draw()
        
    def update(self, i):
        firstPoint = self.points_stack[-1]
        secondPoint = self.points[i]
        
        # decide wheather clockwise
        vectorX = self.vector_stack[-1]
        vectorY = np.array([secondPoint.x - firstPoint.x, secondPoint.y - firstPoint.y])
            
        while(np.cross(vectorX, vectorY) < 0):        # clockwise
            point = self.points_stack.pop()
            point.beProcessed()
            segment = self.segment_stack.pop()
            segment.remove()
            vector = self.vector_stack.pop()
            vector = None # release memory
            
            firstPoint = self.points_stack[-1]
            vectorX = self.vector_stack[-1]
            vectorY = np.array([secondPoint.x - firstPoint.x, secondPoint.y - firstPoint.y])
            
        if(np.cross(vectorX, vectorY) > 0):           # counter-clockwise
            secondPoint.beSelected()
            self.points_stack.append(secondPoint)
            self.segment_stack.append(plt.plot([firstPoint.x, secondPoint.x], [firstPoint.y, secondPoint.y], color = '#ff7f0e', alpha=1, linestyle="solid")[0])
            self.vector_stack.append(np.array([secondPoint.x - firstPoint.x, secondPoint.y - firstPoint.y]))
            
    def frames(self):
        for i in range(1, points_num.get()):
            yield i

    def stop(self):
        # stop animation
        self.ani.event_source.stop()
        
        self.clearStructure()
        self.clearPlot()
        
        # make points--------------------------------------------
        for point in self.points:
            point.setPlot(plt.plot(point.x, point.y, 'o', ms=5 , color = '#1f77b4', alpha=1)[0]) # ms: point size
            
        canvas.draw()
        
# disable Buttom & Entry
def disable(component):
    component['state'] = 'disable'

def enable(component):
    component['state'] = 'normal'
    
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
fig = plt.figure(figsize=(9, 8))
canvas = FigureCanvasTkAgg(fig, setting2)  # A tk.DrawingArea.
canvas.get_tk_widget().grid()

# Algorithm
brain = Graham_scan()
brain.gen_data()

# GUI
tk.Label(setting1, font=("Calibri", 15, "bold"), text="Number of points:", bg="#F0FFF0").pack(side='left', padx=5)
ent = tk.Entry(setting1, width=5, textvariable=points_num)
ent.pack(side='left')
btn1 = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Generate points', command=lambda:[brain.gen_data()])
btn1.pack(side='left', padx=(10, 5), pady=5)
btn2 = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Start finding convex hull', command=lambda:[brain.start(), disable(btn1), disable(btn2), disable(ent),  enable(btn3)])
btn2.pack(side='left', padx=(5, 10), pady=5)
btn3 = tk.Button(setting1, font=("Calibri", 12, "bold"), text='Reset', command=lambda:[brain.stop(), enable(btn1), enable(btn2), enable(ent), disable(btn3)])
btn3.pack(side='left', padx=(5, 10), pady=5)
btn3['state'] = 'disable'

window.mainloop()