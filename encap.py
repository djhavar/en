from tkinter import *
from PIL import Imagetk, Image
from tkinter import ttk
root = Tk

root.title("Encapsulation")
root.geometry("800x800")
root.config(bg="blue")

heading=Label(root, text="juice center", bg="blue", font=("Sylfaen",18,"bold","italic"))
header.place(relx=0.5,rely=0.1,anchor=W)

juice = ImageTk.photoImage(Image.open("logo.png"))
juice_image=Label(root, image=juice, bg="blue")
juice_image.place(relx=0.2,rely=0.4,anchor=CENTER)

apple = ImageTk.photoImage(Image.open("apple.png"))
banana = ImageTk.photoImage(Image.open("banana.png"))
orange = ImageTk.photoImage(Image.open("orange.png"))

fruit=['apple','banana','orange']
fruit_dropdown = ttk.combobox(root,state="readonly",values=fruit,justify="right")
juice_image.place(relx=0.95,rely=0.25,anchor=E)

quantity=Label(root, text="enter quantity", bg="blue", font=("Bahnschrift Light",15))
quantity.place(relx=0.96,rely=0.35,anchor=E)

input=Entry(root)
input.place(relx=0.95,rely=0.4,anchor=E)

quantity_show=Label(root,bg="blue", font=("Bahnschrift Light",12))
quantity_show.place(relx=0.96,rely=0.7,anchor=E)

quantity_label=Label(root, bg="blue", font=("Bahnschrift Light",12))
quantity_label.place(relx=0.95,rely=0.8,anchor=E)
