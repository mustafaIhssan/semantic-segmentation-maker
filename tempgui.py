import Tkinter
parent_widget = Tkinter.Tk()
scale_widget = Tkinter.Scale(parent_widget, from_=0, to=100,
                             orient=Tkinter.HORIZONTAL)
scale_widget.set(25)
scale_widget.pack()
Tkinter.mainloop()