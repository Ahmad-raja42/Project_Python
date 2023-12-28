from tkinter import *
from tkinter .ttk  import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab

class Draw():
    def __init__(self,root):
        self.root = root
        self.root.title("Copy Assignment Painter")
        self.root.configure(background = "White")
        
        self.pointer = "black"
        self.erase = "white"
        
        text = Text(root)
        
        text.insert("1.0", "Drawing Application In Python")
        
        text.tag_add("tag_name","1.0","end")
        text.pack()