import tkinter as tk
import frameGUI as fg
from tkinter.filedialog import askopenfile,askdirectory
import read_file as rf
import analysis as an
import pandas as pd
import prediction as pre
import graph_report as gr
import time

pth=[]


window = tk.Tk()
window.title("stock analysis and prediction system")
window.iconbitmap('C:\\Users\\91727\\PycharmProjects\\majorproj\\958613.png')
window.geometry('700x460')
window.configure(background='turquoise')

def open_file():
    pth.clear()
    file = askopenfile(initialdir='/',title='Select File' ,filetypes=[('csvfiles','*.csv'),('all files', '*.*')])
    label=tk.Label(text=file.name,bg='white')
    label.place(x=14, y=12)
    pth.append(file.name)

# data=rf.read(open_file())
# print(data)
# def buttons():
    # field=open_file().name
    # print(buttonbrows)
    # v=open_file().name


buttonbrows = tk.Button(window, text='Browse', width=13, height=1, command=open_file).place(x=510, y=11)

df=[]

def readcsv():
    df.clear()
    x=pth[0]
    print(x)
    df.append(rf.read(x).reset_index())
    fg.funtable(df[-1])
    # print(df[-1])


readbutn= tk.Button(window, text='Read File', width=25, height=2, command=readcsv)
readbutn.place(x=250, y=50)

field = tk.Text(window, width=60, height=1)
field.place(x=14, y=12)
# field.delete(0.0)
field.insert(0.0, pth[:-1])

pframe=[]
def genrpt():
    dataframe=pd.DataFrame(df[0])
    pframe.append(an.report(dataframe))
    # print(pframe[-1])
    fg.funtable(pframe[-1])


buttonan = tk.Button(window, text="Analyse", width=25, height=2, command=genrpt).place(x=250, y=120)

def gpyrpt():
    gr.greport(pframe[0])

buttongrp = tk.Button(window, text="Graphical Report", width=25, height=2, command=gpyrpt).place(x=250, y=190)

def predt():
    pre.predict(df[0])

buttonpre=tk.Button(window, text='Predict', width=25, height=2, command=predt).place(x=250,y=265)

buttonexit = tk.Button(window, text='EXIT', width=25, height=2, command=window.destroy).place(x=250, y=345)

window.resizable(False,False)

window.mainloop()
