import os
from datetime import datetime
from PIL import Image
import csv
#import exif
import datetime as datetime
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# display the image width, height, and number of channels to our
# terminal
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# show the image and wait for a keypress
cv2.imshow("Image", image)
#cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting image
# filetypes automatically)
cv2.imwrite("newimage-ja.jpg", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image Gray", gray)
#cv2.waitKey(0)

cv2.imwrite("newimage-gray.jpg", gray)

blurred = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Image Gray Blurred", blurred)
#cv2.waitKey(0)

cv2.imwrite("newimage-blurred.jpg", blurred)


thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Image Gray Blurred Threshold", thresh)
#cv2.waitKey(0)

cv2.imwrite("newimage-blurred-thresh.jpg", thresh)


'''
def main():
	processStartTime = datetime.now()
	print(processStartTime)

	try:
		print("main method starting....")
	except IOError as ioe:
		print("IO Error in Main method")
	finally:
		print("main()  finally block executed")
'''