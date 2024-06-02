from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfile
import tkinter as tk
from PIL import Image,ImageTk
import qrcode

window=Tk()
window.title("QR Code Generator")
window.config(bg="Skyblue")

sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
w=sw-800
h=sh-200
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))

def qrfun():
    qrcodegen=str(E1.get())
    img=qrcode.make(qrcodegen)
    rimg=img.resize((120,120), Image.ANTIALIAS)
    simg= ImageTk.PhotoImage(rimg)
    name=str(E2.get())
    img.save("QRcode\\"+name+".jpg")
    msg="QR Code Is Generated"
    var3.set(str(msg))
    box=Label(window,image=simg)
    box.image=img
    box.place(x=230,y=80)

#Heading
H=Label(window,text="OR Code Generator",width=0,height=0,font=("comic sans ms",20,"bold underline"))
H.config(bg="white",fg="black")
H.place(x=160,y=10)

#label
l1=Label(window,text="Enter Link  For  QR",width=0,height=0,font=("comic sans ms",12,"bold"))
l1.config(bg="white",fg="black")
l1.place(x=120,y=250)
var1=StringVar()
E1=Entry(window,textvariable=var1,width=10,font=("comic sans ms",12,"bold"))
E1.config(bg="white",fg="black")
E1.place(x=350,y=250)
B1=Button(window,text="Generate QR And Save",command=qrfun)
B1.place(x=240,y=350)

l2=Label(window,text="Enter Name For QR ",width=0,height=0,font=("comic sans ms",12,"bold"))
l2.config(bg="white",fg="black")
l2.place(x=120,y=300)
var2=StringVar()
E2=Entry(window,textvariable=var2,width=10,font=("comic sans ms",12,"bold"))
E2.config(bg="white",fg="black")
E2.place(x=350,y=300)

var3=StringVar()
l3=Label(window,textvariable=var3,width=20,height=0,font=("comic sans ms",12,"bold"))
l3.config(bg="white",fg="black")
l3.place(x=200,y=400)
#transparent bg
window.wm_attributes("-transparentcolor","skyblue")
window.mainloop()
    
