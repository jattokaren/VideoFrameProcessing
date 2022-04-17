# python video_blur_zoom2.py --video 'HHC Backus PHI 1080p.mp4'
# python video_blur_zoom2.py --video 'VID_20200419_194132_2.mp4'
import cv2
import numpy as np
import argparse
import os
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
    help="path to input image")     # Can have multiple arguments ie filter effect, setting
args = vars(ap.parse_args())

fullfilename = args["video"]
print('Argument Video Filename: ' + str(fullfilename))
filename = fullfilename[:-4]     # Exclude last 4 characters
print(filename)
filetype = fullfilename[-3:]     # Last 3 characters
print(filetype)
filesize = os.path.getsize(fullfilename)
print('Filesize:' + str(filesize))

# create VideoCapture object
cap = cv2.VideoCapture(args["video"])

if (cap.isOpened() == False):
    print('Error while trying to open video. Plese check again...')

# get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print(str(frame_width) + ' x ' + str(frame_height))

# define codec and create VideoWriter object
out = cv2.VideoWriter(str(filename + '_GaussianBlur21.avi'), 
    cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width, frame_height))

# read until end of video
while(cap.isOpened()):
    # capture each frame of the video
    ret, frame = cap.read()
    if ret == True:
        # add gaussian blurring to frame + medianBlur
        #frame = cv2.medianBlur(frame, 9)            #(frame, 7)
        frame = cv2.GaussianBlur(frame, (21,21), 0)   #(3,3) or (5,5) or (7,7) or (101,101)
        #frame = cv2.xphoto.oilPainting(frame, 10, 1) #(frame, 25, 1) or (frame, 10, 1)
        # save video frame
        out.write(frame)
        # display frame
        cv2.imshow('Video', frame)
        # press `q` to exit
        if cv2.waitKey(27) & 0xFF == ord('q'):
            break
    # if no frame found
    else:
        break
# release VideoCapture()
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()