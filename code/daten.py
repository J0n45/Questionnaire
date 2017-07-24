from tkinter import *

class Daten:
    
    def __init__(self,saver, qblocks,window):
        self.window = window
        self.bgcolor ="#EEEEEE"
        self.saver=saver
        self.qblocks=qblocks
    
    def add_lfs(self,lf_l,lf_r):
        self.lf_l = lf_l
        self.lf_r = lf_r
    def add_gui(self,gui):
        self.gui = gui
    def add_window(self,w):
        self.window = w
    def add_fbogen(self,f):
        self.fbogen = f