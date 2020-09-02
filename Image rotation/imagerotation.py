import cv2
import numpy as np
import math
from PIL import Image

img = Image.open(r"assets/rotate.png")
img = np.array(img)
angle_deg = float(input("Enter the angle:- "))

rad = angle_deg* (np.pi/180)

height, width, m = img.shape

new_height = int(width*math.sin(rad) + height*math.cos(rad))
new_width = int(width*math.cos(rad) + height*math.sin(rad))

rot_img = np.zeros((new_height,new_width,m))

mid_row = int((height+1)/2)
mid_col = int((width+1)/2)

for i in range(new_height):
    for j in range(new_width):
        x = round((i-mid_row)*math.cos(rad) + (j-mid_col)*math.sin(rad) + mid_row)
        y = round((j-mid_col)*math.cos(rad) - (i-mid_row)*math.sin(rad) + mid_col) 

        if (x >=0 and x<height and y>=0 and y<width):
            rot_img[i][j][:] = img[x][y][:]


final_img = Image.fromarray(rot_img.astype("uint8"))
final_img.show()