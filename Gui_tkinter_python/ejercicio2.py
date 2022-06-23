#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 06:12:47 2022

@author: kevinsdj
"""
import tkinter

selectList=["item1","item2","item2","item3","item4","item5"]

window= tkinter.Tk()
window.minsize(300,600)
window.maxsize(300,600)
window.title('My list')

label_header= tkinter.Label(window,text='list',bg='green',fg='white')
label_header.pack(fill='x')

inputitem= tkinter.Entry(window,text='add a item to list')
inputitem.pack()

listbox=tkinter.Listbox(window)

button_add=tkinter.Button(window,text='add')
button_add.pack()
def insertItem(event):
    selectList.append(inputitem.get())
    index=selectList.__len__()-1
    listbox.insert(index,selectList[index])
    
button_add.bind('<Button-1>',insertItem)

for value in selectList:
    listbox.insert(selectList.index(value), value)
listbox.pack(fill='x')

window.mainloop()
    

