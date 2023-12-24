import time_matrix
import os
from PIL import Image
################################################################################################################################
current_directory = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_directory,'Export.png')
image_path = os.path.join(current_directory,'Op/Frame00000.png')
input_image = Image.open(image_path)
width, height = input_image.size
################################################################################################################################
max_tic = 4
wdt = int(width/100)
img  = Image.new( mode = "RGB", size = (width, height), color = (255, 255, 255) )
img_pm = img.load()
color = [(255,20,20), (20,255,20), (20,20,255), (100, 100, 100), (34, 67, 19), (255, 255, 255), (56, 88, 199), (3, 46, 200)]
time_matrix = time_matrix.time_data()
################################################################################################################################
for i in range (0,8):
    for c in range (max_tic):
        start =  time_matrix[i][c].split()
        if (start == []):
            continue
        for j in range(wdt):
            for k in range(wdt):
                img_pm[int(float(start[0]))-j,int(float(start[1]))-k] = color[c]
                img_pm[int(float(start[0]))+j,int(float(start[1]))+k] = color[c]
                img_pm[int(float(start[0]))-k,int(float(start[1]))+j] = color[c]
                img_pm[int(float(start[0]))+k,int(float(start[1]))-j] = color[c]
img.save(output_path, format="png")
################################################################################################################################