#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:17:39 2022

@author: priyankadas
"""

from tkinter import *

root = Tk()

root.title("Inheretence")
root.geometry("600x400")

user_name = Label(root, text = "User Name :")
email1 = Label(root, text = "Email Id :")

ue = Entry(root)
ee = Entry(root)

l1 = Label(root)

list1 = {}

def detail():
    name = ue.get()
    email = ee.get()
    list1[name] = email
    l1["text"] = list1
    
btn = Button(root, text = "Add User Detail", command = detail)
user_name.pack()
email1.pack()
ue.pack()
ee.pack()
l1.pack()
btn.pack()
root.mainloop()