import cv2
import numpy as np
import math
from PIL import Image

img = Image.open(r"assets/mask.jpg")
img = np.array(img)

def rgb2bgr(img):
    res = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i][j][0] = img[i][j][2]
            res[i][j][1] = img[i][j][1]
            res[i][j][2] = img[i][j][0]
    return res

mask = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.cvtColor(mask,cv2.COLOR_HSV2BGR)

def color_detection(img,lower,upper):
    mask = np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] >= lower[0] and img[i][j][1] >= lower[1] and img[i][j][2] >= lower[2] and img[i][j][0] <= upper[0] and img[i][j][1] <= upper[1] and img[i][j][2] <= upper[2]:
                mask[i][j][0] = 255
                mask[i][j][1] = 255
                mask[i][j][2] = 255
            else:
                mask[i][j][0] = 0
                mask[i][j][1] = 0
                mask[i][j][2] = 0
    img = np.bitwise_and(mask,img)
    res = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return res


lower = np.array([94,130,38])
upper = np.array([179,255,255])
res = color_detection(img,lower,upper)
final_img = Image.fromarray(res.astype(np.uint8))
final_img.show()


