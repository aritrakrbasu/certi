
from PIL import ImageFont, ImageDraw, Image  
import cv2  
import numpy as np  
import os
import csv

f = open("names.txt","r")
names_list = f.read().split("\n")
print(len(names_list))

f1 = open("coords.txt","r")
coordinates = f1.read().split("\n")

flag=True

for i in range(len(names_list)):


    name_to_print = names_list[i]

    # Load image in OpenCV  
    image = cv2.imread("certificate.png")  

    # Convert the image to RGB (OpenCV uses BGR)  
    cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  

    # Pass the image to PIL  
    pil_im = Image.fromarray(cv2_im_rgb)  

    draw = ImageDraw.Draw(pil_im)  
    # use a truetype font  
    font = ImageFont.truetype("./fonts/Playlist Script.otf", 120)      #You can change fonts from list given bottom

    # Draw the text 
    draw.text((int(coordinates[0]), int(coordinates[1])), name_to_print.title(), font=font , fill='#FF914D')
    
    # Get back the image to OpenCV  
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  
    

    print("done -"+str(i)+"--"+name_to_print.title())
    path = ''
    cv2.imwrite('./organizers_2ndyear/'+name_to_print.title()+'.png',cv2_im_processed)
    #os.startfile('output.png')
    cv2.waitKey(0)  

    cv2.destroyAllWindows()
    

'''
Other vareity of FONTS (Make sure you give proper path)

MLSJN.TTF
Lato-Black.ttf
MATURASC.TTF
OLDENGL.TTF
VIVALDII.TTF
copperplate gothic font.ttf


'''


