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

def sobelfilter(img):
    img = rgb2gray(img)
    img = convolvefunct(img, gaussian_blurr)
    img_x = convolvefunct(img,X_direct_kernel)
    img_y = convolvefunct(img,Y_direct_kernel)

    res = np.hypot(img_x,img_y)
    res = res/res.max()*255
    angle = np.arctan2(img_y,img_x)

    return (res,angle)


def non_max_suppression(img, ang):
    M,N = img.shape
    res = np.zeros((M,N),dtype= np.int32)
    angle = ang*180/np.pi
    angle[angle<0]+=180

    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
               #angle 0
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                #angle 45
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                #angle 90
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                #angle 135
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                if (img[i,j] >= q) and (img[i,j] >= r):
                    res[i,j] = img[i,j]
                else:
                    res[i,j] = 0

            except IndexError as e:
                pass
    
    return res

def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    
    highThreshold = img.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio
    
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)

def hysteresis(img, weak, strong=255):
    M, N = img.shape  
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img

def cannyfilter(img):
    img, angle = sobelfilter(img)
    img = non_max_suppression(img,angle)
    res,weak,strong = threshold(img)
    res = hysteresis(res,weak,strong)

    return res

img = Image.open(r"assets/edge-detection.png")
img = np.array(img)

result = cannyfilter(img)
final_img = Image.fromarray(result.astype(np.uint8))
#final_img.save("Edge Detection/canny.png")
final_img.show()