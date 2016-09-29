import gui
import cv2
from skimage import img_as_ubyte
from Tkinter import *        
from PIL import ImageTk, Image



# segment the image
image = cv2.imread('2.jpg')
[segments, segmentats_with_bounderies] = gui.segmentation_now(image)
segmentats_with_bounderies = img_as_ubyte(segmentats_with_bounderies)


# GUI Stuff
root = Tk()

#Setting it up
img = ImageTk.PhotoImage(Image.fromarray(segmentats_with_bounderies,'RGB'))

#Displaying it
imglabel = Label(root, image=img).grid(row=1, column=1)        



root.bind('<Key>', gui.key)
# root.bind('<Button-1>', motion)
root.bind('<Button-1>', lambda event : gui.click2Segment(event, segments, image))







# Run 
root.mainloop()



