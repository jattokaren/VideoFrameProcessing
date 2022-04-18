# Imaging Processing with Python 
a .gif cycling thru some image manipulation examples

<img src="/Image Examples/PXL_20220414_015637240_2-ANIMATION.gif" width="400" height="300">

# Practice doing image/video processing
* How to open/load an image and do some munipulation and output something (ie file(s), image(s) and/or video(s)).

  ## Python Examples
* [Example Functions](#example-functions)
* [Image Filters / Manipulation](#project-1)
* [Video Processing ](#project-2)
* [Next Steps](#next-steps)

## Example Functions
* oilPainting
<br>
<img src="/PXL_20220402_222514868.MP-oilpainting_02_25.jpg" width="400" height="300">
Resizing Image to 400x300
cv2.xphoto.oilPainting(frame, 10, 1)
<br>
* GaussianBlur
** cv2.GaussianBlur(frame, (21,21), 0)    

<div style="width:60px ; height:60px">
![Python oilPainting](/PXL_20220402_222514868.MP-oilpainting_02_25.jpg?raw=true "Python Photo to Image Oil Painting Effect")
<div>
  
![Python oilPainting](/PXL_20220402_222514868.MP-oilpainting_02_25.jpg?raw=true "Python Photo to Image Oil Painting Effect")
  <br>

## Project 1
* **Input:** an image file
	* PXL_20220402_222514868.MP.jpg
	* python imageFilterOptions.py --image PXL_20220414_015637240_2.jpg
* **Output:** 6 image files
	* oilpainting 50
	* oilpainting 25
	* oilpainting 10
	* RGB Gray Scale
	* RGB Heatmap
	* BGR Gray Scale
	* BRG Heatmap

	PXL_20220402_222514868.MP-oilpainting_01_50.jpg
	PXL_20220402_222514868.MP-oilpainting_02_25.jpg
	PXL_20220402_222514868.MP-oilpainting_03_10.jpg
	PXL_20220402_222514868.MP-RGB-GRAY.jpg
	PXL_20220402_222514868.MP-RGB-Heatmap.jpg
	PXL_20220402_222514868.MP-BGR-GRAY.jpg
	PXL_20220402_222514868.MP-BRG-Heatmap.jpg	

| Image Filename | Python Code | Rendered Image | Image Size |
|-----:|-----:|-----:|-----:|
|PXL_20220402_222514868.MP.jpg|image = cv2.imread(args["image"])|<img src="/Image Examples/PXL_20220402_222514868.MP.jpg" width="240" height="180">   |6.4 MB|
|PXL_20220402_222514868.MP-oilpainting_01_50.jpg|oilpaint50 = cv2.xphoto.oilPainting(image, 50, 1)|<img src="/Image Examples/PXL_20220402_222514868.MP-oilpainting_01_50.jpg" width="240" height="180">   |2.0 MB|
|PXL_20220402_222514868.MP-oilpainting_02_25.jpg|oilpaint25 = cv2.xphoto.oilPainting(image, 25, 1)|<img src="/Image Examples/PXL_20220402_222514868.MP-oilpainting_02_25.jpg" width="240" height="180"> |2.8 MB|
|PXL_20220402_222514868.MP-oilpainting_03_10.jpg|oilpaint10 = cv2.xphoto.oilPainting(image, 10, 1)|<img src="/Image Examples/PXL_20220402_222514868.MP-oilpainting_03_10.jpg" width="300" height="200"> |4.2 MB|
|PXL_20220402_222514868.MP-RGB-GRAY.jpg|img_RGB_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)|<img src="/Image Examples/PXL_20220402_222514868.MP-RGB-GRAY.jpg" width="300" height="200"> |3.1 MB|
|PXL_20220402_222514868.MP-RGB-Heatmap.jpg|img_RGB_Heatmap = cv2.applyColorMap(img_RGB_Gray, cv2.COLORMAP_JET)|<img src="/Image Examples/PXL_20220402_222514868.MP-RGB-Heatmap.jpg" width="300" height="200"> |6.6 MB|
|PXL_20220402_222514868.MP-BGR-GRAY.jpg|img_BGR = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)|<img src="/Image Examples/PXL_20220402_222514868.MP-BGR-GRAY.jpg" width="300" height="200"> |3.1 MB|
|PXL_20220402_222514868.MP-BRG-Heatmap.jpg|img_BGR_Heatmap = cv2.applyColorMap(img_BGR_Gray, cv2.COLORMAP_JET)|<img src="/Image Examples/PXL_20220402_222514868.MP-BRG-Heatmap.jpg" width="300" height="200"> |6.7 MB|	
	
## Project 2
* **Input:** a video file
	* python video_blur_zoom2.py --video 'HHC Backus PHI 1080p.mp4'
	* python video_blur_zoom2.py --video 'VID_20200419_194132_2.mp4'
* **Output:** a video file with some image processing
	* 2022-03-14 HP PHI Clip_GaussianBlur101.avi

## Next Steps
* Counting Pixel / Colors
* Count Yellow Circles
* Animate Objects (Spin & Move)


	
	
	/Image Examples/PXL_20220402_222514868.MP.jpg
	/Image Examples/PXL_20220402_222514868.MP-oilpainting_01_50.jpg
	/Image Examples/PXL_20220402_222514868.MP-oilpainting_02_25.jpg
	/Image Examples/PXL_20220402_222514868.MP-oilpainting_03_10.jpg
	/Image Examples/PXL_20220402_222514868.MP-RGB-GRAY.jpg
	/Image Examples/PXL_20220402_222514868.MP-RGB-Heatmap.jpg
	/Image Examples/PXL_20220402_222514868.MP-BGR-GRAY.jpg
	/Image Examples/PXL_20220402_222514868.MP-BRG-Heatmap.jpg

	

