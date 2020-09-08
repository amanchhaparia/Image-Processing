## Image Processing Task
The following operations are implemented without using the built-in library,Numpy and Pillow are used to load and save the image

### 1. Image Rotation

The image can be rotated by any angle bound or inbound.

|<img width="640" height="450" src="https://github.com/amanchhaparia/Image-Processing/blob/master/assets/rotate.png">| 
|:---:|
|Input Image|

*Output*
|<img width="600" height="322" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Image%20rotation/rotated_nobound.png">|<img width="640" height="450" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Image%20rotation/rotated_bounded.png">|
|:---:|:---:|
|No Bound|Bound|

### 2. Applying Kernels

Applying 5X5 filters to do the following task
1. Blurring 
2. Sharpening


|<img width="446" height="447" src="https://github.com/amanchhaparia/Image-Processing/blob/master/assets/filter.png">|
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

|<img width="602" height="452" src="https://github.com/amanchhaparia/Image-Processing/blob/master/assets/edge-detection.png">|
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
|<img width="112" height="150" src="https://github.com/amanchhaparia/Image-Processing/blob/master/assets/morphological.png">|<img width="112" height="150" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Morphological%20transformation/dilation.png">|<img width="112" height="150" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Morphological%20transformation/erosion.png">|<img width="112" height="150" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Morphological%20transformation/edge_detection.png">|
|:---:|:---:|:---:|:---:|
|Input-Image|Dilation|Erosion|Edge-Detection|

### 5.  Masking
A *mask* is a binary image consisting of zero- and non-zero values. If a mask is applied to another binary or to a grayscale image of the same size, all pixels which are zero in the mask are set to zero in the output image. All others remain unchanged.   
*Masking* is often used to restrict a point or arithmetic operator to an area defined by the mask. We can, for example, accomplish this by first masking the desired area in the input image and processing it with the operator, then masking the original input image with the inverted mask to obtain the unprocessed area of the image and finally recombining the two partial images using image addition.

|<img width="600" height="322" src="https://github.com/amanchhaparia/Image-Processing/blob/master/assets/mask.jpg">|<img width="640" height="450" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Masking/masked.png">|
|:---:|:---:|
|Input-Image|Masked Image(Blue ball detected)|

### 6.  Region of Interest(ROI)
A region of interest (ROI) is a portion of an image that you want to filter or perform some other operation on. You define an ROI by creating a binary mask, which is a binary image that is the same size as the image you want to process with pixels that define the ROI set to 1 and all other pixels set to 0.

|<img width="600" height="322" src="https://github.com/amanchhaparia/Image-Processing/blob/master/assets/roi.jpg">|<img width="600" height="322" src="https://github.com/amanchhaparia/Image-Processing/blob/master/Region%20of%20interest(ROI)/roi_moved.png">|
|:---:|:---:|
|Input-Image|Output Image|


