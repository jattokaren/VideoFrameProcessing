<img src="/Image Examples/PXL_20220414_015637240_2-ANIMATION.gif" width="400" height="300">

# Practice doing image/video processing
* How to open/load an image and do some munipulation and output something (ie file, image(s), video).

## Python Image Filters / Effects
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


  ## Next Steps
* Counting Pixel / Colors
* Count Yellow Circles
* Animate Objects (Spin & Move)

| Image File Attributes   |      1st Image     |  2nd Image | 3rd Image |
|----------|:-------------:|------:|----:|
| Filename |  PXL_20220414_015637240_2.jpg| -oilpainting_01_50.jpg | 
| Python Code |  image = cv2.imread(args["image"])| oilpaint50 = cv2.xphoto.oilPainting(image, 50, 1) |
| Rendered Image |    <img src="/PXL_20220402_222514868.MP-oilpainting_02_25.jpg" width="240" height="180">   |   $12 |
| Image Size | 2.9 MB |    2.0 MB |	
| # of Pixels | 100k |    $1 |	
	
	

	
| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |
	
	
Solarized dark             |  Solarized Ocean
:-------------------------:|:-------------------------:
![](https://...Dark.png)  |  ![](https://...Ocean.png)
	
	
  ## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with:
* Lorem version: 12.3
* Ipsum version: 2.33
* Ament library version: 999
	
## Setup
To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```
