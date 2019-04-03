from tkinter import *
from tkinter import messagebox
import tkinter as tk
import cv2
import os
import numpy as np
from PIL import Image
import os
import sqlite3
from pymongo import MongoClient
from bson.son import SON
from pprint import pprint



root=Tk()

frame = Frame(root,bg="#728B8E",width=800,height=600)
'''This class configures and populates the toplevel window.
is the toplevel containing window.'''
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'

root.geometry("800x450")

Button1 = tk.Button(root)
Button1.place(relx=0.391, rely=0.590, height=42, width=208)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''submit''')

Entry1 = tk.Entry(root)
Entry1.place(relx=0.334, rely=0.373,height=56, relwidth=0.362)
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="font13")
Entry1.configure(foreground="#000000")
Entry1.configure(highlightbackground="#d9d9d9")
Entry1.configure(highlightcolor="black")
Entry1.configure(insertbackground="black")
Entry1.configure(selectbackground="#c4c4c4")
Entry1.configure(selectforeground="black")

Label1 = tk.Label(root)
Label1.place(relx=0.034, rely=0.106, height=101, width=787)
Label1.configure(activebackground="#728B8E")
Label1.configure(activeforeground="black")
Label1.configure(background="#728B8E")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font="-family {Segoe UI Black} -size 30 -weight bold")
Label1.configure(foreground="#000000")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
Label1.configure(text='''Enter Your UIN No''')

frame.pack()
