import cv2
import numpy as np
import math
from PIL import Image

gaussian_blurr=np.array([[1,  4,  6,  4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1,  4,  6,  4, 1]])/256

X_direct_kernel = np.array([[-1,0,1],
                            [-2,0,2],
                            [-1,0,1]])

Y_direct_kernel = np.array([[-1,-2,-1],
                            [0,0,0],
                            [1,2,1]])                    

def convolvefunct(img, kernel):
    pad = (kernel.shape[1]-1)//2
    img_pad = cv2.copyMakeBorder(img,pad,pad,pad,pad,cv2.BORDER_REPLICATE)
    result = np.zeros_like(img_pad)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            result[y,x]= (kernel*img_pad[y:y+kernel.shape[0],x:x+kernel.shape[1]]).sum()
    return result


def rgb2gray(img):
    return np.dot(img[:,:,:3],[0.2989,0.5870,0.1140])

def horizontalEdgeDetection(img,kernel):
    result = convolvefunct(img,kernel)
    return result







img = Image.open(r"assets/edge-detection.png")
img = np.array(img)
img = rgb2gray(img)
img = convolvefunct(img,gaussian_blurr)
result_x = horizontalEdgeDetection(img,X_direct_kernel)
result_y = horizontalEdgeDetection(img,Y_direct_kernel)
result = np.hypot(result_x,result_y)
result = result/result.max()*255
final_img = Image.fromarray(result.astype(np.uint8))
final_img.save("Edge Detection/sobel.png")
final_img.show()