import os
from PIL import ImageFont, ImageDraw, Image  

f = open("names.txt","r")
names_list = f.read().split("\n")

i=0
for name in names_list:
    names_list[i] = name.title()+".png"
    i=i+1



arr = os.listdir("./quiz")

print(list(set(names_list)-set(arr)))
# print(len(list(set(arr)-set(names_list))))

# print(arr)