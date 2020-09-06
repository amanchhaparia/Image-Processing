## Image Processing Task
The following operations are implemented without using the built-in library,Numpy and Pillow are used to load and save the image

### 1. Image Rotation

The image can be rotated by any angle bound or inbound.
|<img width="640" height="450" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/1.Image_Rotation/rotate.png">| 
|:---:|
|Input Image|

*Output*
|<img width="600" height="322" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/1.Image_Rotation/rotated_without_bound.png">|<img width="640" height="450" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/1.Image_Rotation/rotated_with_bound.png">|
|:---:|:---:|
|No Bound|Bound|

### 2. Applying Kernels

Applying 5X5 filters to do the following task
1. Blurring 
2. Sharpening

|<img width="446" height="447" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/2.Applying_Kernels/test_sharpen.png">|
|:---:|
|Input Image|

*Output*
|<img width="640" height="450" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Kernels/box_blur.png">|<img width="640" height="450" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Kernels/gaussian_blur.png">|<img width="640" height="450" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Kernels/Sharpen.png">|
|:---:|:---:|:---:|
|Box Filter|Gaussian Filter|Sharpen|

### 3. Edge Detection
Applying Edge Detection in following sequence 
1. Vertical edge detection
2. Horizontal edge detection
3. Sobel edge detection (right, left, top, bottom)
4. Canny edge detection  

|<img width="602" height="452" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/3.Edge_Detection/edge-detection1.png">|
|:---:|
|Input Image|

*Output*
|<img width="602" height="452" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Edge%20Detection/vertical.png">|<img width="602" height="452" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Edge%20Detection/horizontal.png">|
|:---:|:---:|
|Vertical Edge Detection|Horizontal Edge Detection|
|<img width="602" height="452" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Edge%20Detection/sobel.png">|<img width="602" height="452" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Edge%20Detection/canny.png">|
|Sobel Edge Detection|Canny Edge Detection|

### 4. Morphological Transformation
Applying dilation and erosion transformation to the image

*Output*
|<img width="112" height="150" src="https://github.com/gautam-dev-maker/Image_Processing/blob/master/4.Morphological_Transformation/morphological.png">|<img width="112" height="150" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Morphological%20transformation/dilation.png">|<img width="112" height="150" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Morphological%20transformation/erosion.png">|<img width="112" height="150" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Morphological%20transformation/edge_detection.png">|
|:---:|:---:|:---:|:---:|
|Input-Image|Dilation|Erosion|Edge-Detection|
