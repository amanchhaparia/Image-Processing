import cv2
import numpy as np
import math
from PIL import Image

structElem = np.array([[0,1,0],
                       [1,1,1],
                       [0,1,0]])

def dilation(img, kernel):
    pad = (kernel.shape[1]-1)//2
    img_pad = cv2.copyMakeBorder(img,pad,pad,pad,pad,cv2.BORDER_REPLICATE)
    img_pad = rgb2gray(img_pad)
    img_pad = gray2binary(img_pad)
    result = np.zeros_like(img_pad)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            sum= (kernel*img_pad[y:y+kernel.shape[0],x:x+kernel.shape[1]]).sum()
            if sum ==5:
                result[y,x]=1
            else:
                result[y,x]=0
    return result

def rgb2gray(img):
    return np.dot(img[:,:,:3],[0.2989,0.5870,0.1140])

def gray2binary(gray):
    return (gray>127) & (gray<=255)


img = Image.open(r"assets/morphological.png")
img = np.array(img)

result = dilation(img,structElem)
final_img = Image.fromarray(result).convert('RGB')
final_img.save("Morphological transformation/erosion.png")
final_img.show()