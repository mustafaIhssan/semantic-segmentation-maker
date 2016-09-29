import cv2 
from Tkinter import *        
from PIL import ImageTk, Image
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
import argparse
from skimage import img_as_ubyte


x = 0
y = 0
# fun hell

def key(event):
    root.event_generate('<Motion>', warp=True, x=50, y=50)

def motion(event):
    print('motion {}, {}'.format(event.x, event.y))

def segmentation_now(image):
	segments = slic(img_as_float(image), n_segments = 500, sigma = 2)
	segmentats_with_bounderies = mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments)
	cv2.imwrite("seg/segment.jpg",segmentats_with_bounderies)

	allsegs = []
	# loop over the unique segment values
	for (i, segVal) in enumerate(np.unique(segments)):
		# construct a mask for the segment
		# print "[x] inspecting segment %d" % (i)
		mask = np.zeros(image.shape[:2], dtype = "uint8")
		mask[segments == segVal] = 255
	
		segment = cv2.bitwise_and(image, image, mask = mask)

		allsegs.append(segment)

	allsegs = np.array(allsegs)

	return allsegs, segmentats_with_bounderies

def click2Segment(event, segments, image):
	x = event.x 
	y = event.y
	for index, segment in enumerate(segments):
		sum_of_pixel = np.sum(segment[y][x])
		if sum_of_pixel > 0:
			clicked_index = index
			clicked_segment = segment
	Change_part_color(clicked_index, clicked_segment, [00,22,66])

def Change_part_color(index, segment, color):
	[r,g,b] = color
	[y,x,z] = image.shape
	# loop through every pixel
	for y in xrange(1,y):
		for x in xrange(1,x):
			im_p = image[y][x][0]
			seg_p = segment[y][x][0]
			# on corosponding pixel in both oreginal and segment
			if (im_p == seg_p):
				print im_p
				print seg_p
				image[y][x] = [r,g,b] 
	cv2.imshow('seg_%d.jpg' % index, image)
	cv2.waitKey(0)
				


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())


# segment the image
image = cv2.imread(args["image"])
[segments, segmentats_with_bounderies] = segmentation_now(image)
segmentats_with_bounderies = img_as_ubyte(segmentats_with_bounderies)

# GUI Stuff
root = Tk()

#Setting it up
img = ImageTk.PhotoImage(Image.fromarray(segmentats_with_bounderies,'RGB'))

#Displaying it
imglabel = Label(root, image=img).grid(row=1, column=1)        



root.bind('<Key>', key)
# root.bind('<Button-1>', motion)
root.bind('<Button-1>', lambda event : click2Segment(event, segments, image))







# Run 
root.mainloop()



