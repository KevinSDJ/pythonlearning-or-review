#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:05:32 2022

@author: kevinsdj
"""

import tkinter
valores={'option1':'2','option2':'3'}

window= tkinter.Tk()
window.maxsize(900,600)
window.minsize(600,400)
seleccionado=tkinter.StringVar()
seleccionado.set('0')
label_value_txt=tkinter.Label(window,text='value')
value_view=tkinter.Label(window,text=seleccionado.get())
value_view.pack()
label_value_txt.pack()
def changeValueCheck(event):
    value_view['text']=seleccionado.get()
def reset(event):
    seleccionado.set('0')
    value_view['text']='0'
for key in valores:
    vlue=valores[key]
    txt=key
    radio_buton=tkinter.Radiobutton(window,text=txt,value=vlue,variable=seleccionado)
    radio_buton.bind('<Button-1>',changeValueCheck)
    radio_buton.pack()
reset_button= tkinter.Button(window,text='reset values')
reset_button.bind('<Button-1>',reset)
reset_button.pack()
window.mainloop()
