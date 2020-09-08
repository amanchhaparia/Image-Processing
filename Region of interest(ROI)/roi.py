import cv2
import numpy as np
import math
from PIL import Image



def roi(img,mask):
    mask[:,:,:] = img[887:1033,1036:1188,:]
    img[865:1011,326:478,:] = mask[:,:,:]
    return img

def convolute(img, kernel):
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

gaussian_blurr=np.array([[1,  4,  6,  4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1,  4,  6,  4, 1]])/256



img = Image.open(r"assets/roi.jpg")
img = np.array(img)
img = convolute(img,gaussian_blurr)
mask = np.zeros((146,152,img.shape[2]),dtype=np.uint8)

res = roi(img,mask)
final_img = Image.fromarray(res)
final_img.show()
final_img.save("Region of interest(ROI)/roi_moved.png")

