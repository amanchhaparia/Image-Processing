import cv2
import numpy as np
import math
from PIL import Image

def sheerRotationCoordinate(x,y,angle):

    tangent=math.tan(angle/2)
    new_x=round(x-y*tangent)
    new_y=y

    new_y=round(new_x*math.sin(angle)+new_y)

    new_x=round(new_x-new_y*tangent) 

    return new_y,new_x


img = Image.open(r"assets/rotate.png")
img = np.array(img)
angle_deg = float(input("Enter the angle:- "))

rad = angle_deg* (np.pi/180)

height, width, m = img.shape


new_height = round(abs(height*math.cos(rad))+abs(width*math.sin(rad)))
new_width = round(abs(height*math.sin(rad))+abs(width*math.cos(rad)))

rot_img = np.zeros((new_height,new_width,m))

old_mid_row = int(((height+1)/2)-1)
old_mid_col = int(((width+1)/2)-1)

new_mid_row = int((new_height+1)/2-1)
new_mid_col = int((new_width+1)/2-1)

for row in range(height):
    for col in range(width):
        y = row-old_mid_row
        x = col-old_mid_col

        new_y,new_x = sheerRotationCoordinate(y,x,rad)

        new_x = new_mid_col +new_x
        new_y = new_mid_row +new_y

        if (new_x >=0 and new_x<new_width and new_y>=0 and new_y<new_height):
            rot_img[new_y][new_x][:] = img[row][col][:]


final_img = Image.fromarray(rot_img.astype("uint8"))
final_img.show()
final_img.save("Image rotation/rotated_bounded.png")