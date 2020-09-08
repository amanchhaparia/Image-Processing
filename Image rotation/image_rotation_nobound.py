import cv2
import numpy as np
import math
from PIL import Image

img = Image.open(r"assets/rotate.png")
img = np.array(img)
angle_deg = float(input("Enter the angle:- "))

rad = angle_deg* (np.pi/180)

height, width, m = img.shape


new_height = height
new_width = width

rot_img = np.zeros((new_height,new_width,m))

old_mid_row = int(((height+1)/2)-1)
old_mid_col = int(((width+1)/2)-1)

new_mid_row = int((new_height+1)/2-1)
new_mid_col = int((new_width+1)/2-1)

for row in range(height):
    for col in range(width):
        y = round((row-old_mid_row)*math.cos(rad) - (col-old_mid_col)*math.sin(rad))
        x = round((col-old_mid_col)*math.cos(rad) + (row-old_mid_row)*math.sin(rad)) 

        new_x = new_mid_col +x
        new_y = new_mid_row +y

        if (new_x >=0 and new_x<new_width and new_y>=0 and new_y<new_height):
            rot_img[new_y][new_x][:] = img[row][col][:]


final_img = Image.fromarray(rot_img.astype("uint8"))
final_img.show()