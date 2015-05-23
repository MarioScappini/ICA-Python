from tkinter import *

root = Tk();
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

bottom1 = Button(topFrame,text="Buttom",fg="red")

bottom3 = Button(topFrame,text="Buttom",fg="red")

bottom4 = Button(topFrame,text="Buttom",fg="red")
bottom2 = Button(bottomFrame,text="Buttom",fg="green")
bottom1.pack(side=LEFT)
bottom3.pack(side=LEFT)
bottom4.pack()
bottom2.pack()
root.mainloop()