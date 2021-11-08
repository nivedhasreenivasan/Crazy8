from tkinter import *
import csv
from PIL import ImageTk, Image

root = Tk()
root.title("Crazy 8")
c = Canvas(root)
root.geometry('1500x900')
c.pack(fill=BOTH, expand=True)
#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)
#Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu= options_menu)
options_menu.add_command(label="Reset")

def skip():
    global skipButton
    global clicked
    clicked = True
    skipButton = Button(root, text="SKIP", font=("Helvetica", 7), height = 3, width = 9, bg="SystemButtonFace", command=lambda: skip_click(skipButton))
    skipButton.place(x=710,y=650)


skip()

root.mainloop()
