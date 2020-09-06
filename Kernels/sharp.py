import cv2
import numpy as np
import math
from PIL import Image

gaussian_blurr=np.array([[1,  4,  6,  4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1,  4,  6,  4, 1]])/256

Sharpen = np.array([[-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1],
                  [-1,-1,25,-1,-1],
                  [-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1]])/-25

box_blur=np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]])/9


def filter(img, kernel):
    pad = (kernel.shape[1]-1)//2
    img_pad = cv2.copyMakeBorder(img,pad,pad,pad,pad,cv2.BORDER_REPLICATE)
    result = np.zeros_like(img_pad)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            for z in range(img.shape[2]):
                result[y,x,z]= (kernel*img_pad[y:y+kernel.shape[0],x:x+kernel.shape[1],z]).sum()
    if(img_pad.shape[2]==4):
        result[::3] = img_pad[::3]
    return result


img = Image.open(r"assets/filter.png")
img = np.array(img)
result = filter(img, Sharpen)
final_img = Image.fromarray(result.astype(np.uint8))
final_img.save("Kernels/Sharpen.png")
final_img.show()
