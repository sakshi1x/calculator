from tkinter import *
from tkinter import messagebox
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
root = Tk()
root.title("photos")
root.geometry("500x250")


img = Image.open('E:\calculator\c\image1.jfif')
#Resize the Image using resize method
resized_image= img.resize((500,250), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
imgg = Label(root,image = new_image).place(x =0,y = 0)
root.mainloop()