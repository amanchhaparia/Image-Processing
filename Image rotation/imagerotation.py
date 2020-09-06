import cv2
import numpy as np
import math
from PIL import Image

img = Image.open(r"assets/rotate.png")
img = np.array(img)
angle_deg = float(input("Enter the angle:- "))

rad = angle_deg* (np.pi/180)

height, width, m = img.shape
print(img.shape)
new_height = round(height*math.cos(rad)+width*math.sin(rad))
new_width = round(height*math.sin(rad)+width*math.cos(rad))

rot_img = np.zeros((height,width,m))

mid_row = int(((height+1)/2)-1)
mid_col = int(((width+1)/2)-1)

for row in range(height):
    for col in range(width):
        x = round((row-mid_row)*math.cos(rad) + (col-mid_col)*math.sin(rad) + mid_row)
        y = round((col-mid_col)*math.cos(rad) - (row-mid_row)*math.sin(rad) + mid_col) 

        if (x >=0 and x<height and y>=0 and y<width):
            rot_img[x][y][:] = img[row][col][:]


final_img = Image.fromarray(rot_img.astype("uint8"))
final_img.show()