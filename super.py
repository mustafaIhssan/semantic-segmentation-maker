# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2 
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image and apply SLIC and extract (approximately)
# the supplied number of segments
image = cv2.imread(args["image"])
segments = slic(img_as_float(image), n_segments = 500, sigma = 2)
 
# show the output of SLIC
fig = plt.figure("Superpixels")
ax = fig.add_subplot(1, 1, 1)
ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments))
plt.axis("off")
plt.show()

allsegs = []
# loop over the unique segment values
for (i, segVal) in enumerate(np.unique(segments)):
	# construct a mask for the segment
	print "[x] inspecting segment %d" % (i)
	mask = np.zeros(image.shape[:2], dtype = "uint8")
	mask[segments == segVal] = 255
	
	segment = cv2.bitwise_and(image, image, mask = mask)
	allsegs.append(segment)

	# uncomment to save segments 
	# cv2.imwrite("seg/segment_%d.jpg" % (i),segment)

	# uncomment to show the masked region
	#cv2.imshow("Mask", mask)
	#cv2.imshow("Applied", segment)
	#cv2.waitKey(0)


def saveImArray(segments):
	for segment in segments:
		pass
		plt.imshow(segment)
	 	plt.savefig("seg/segment_%d.jpg" % (i))
		
	pass