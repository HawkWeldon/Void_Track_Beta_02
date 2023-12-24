import torch
import numpy as np
from PIL import Image
import os #Main imports
################################################################################################################
current_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_directory, 'model/model.pt')
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path) #current_driectory read and model call
################################################################################################################
from utlz.vid_frm import form
from utlz.V2f import video
from utlz.flark import main 
from utlz.raw_data import raw 
from utlz.time_matrix import time_data #custom utilitties
################################################################################################################
def euq_distance(a,b):
    dist = np.sqrt(np.square(int(float(a.split()[0]))-int(float(b.split()[0]))) + np.square(int(float(a.split()[1]))-int(float(b.split()[1]))))
    return dist
################################################################################################################
file = open("temp.txt","r+")
file.truncate(0)
file.close()
no_frm = video(current_directory)
print ("no of fromes :"+str(no_frm)) 
idx = 0 #forming frames and starting open variable in the form of temp.txt
################################################################################################################
while(idx<no_frm):
    image_path = 'Op/Frame%05d.png'%idx
    image_path = os.path.join(current_directory, image_path)
    raw_path = 'raw_data/raw_data%05d.txt'%idx
    raw_path = os.path.join(current_directory, raw_path)
    df = main(image_path, model)
    mid_points = df.splitlines()
    raw(mid_points, raw_path)
    print('#'*150)
    print('reading frame :'+str(idx))
    print('#'*150)
    idx = idx + 1
#raw frame data extraction
################################################################################################################
idx = 1
data , max_tick = time_data(current_directory)
#distance = np.zeros(shape=(no_frm,max_tick))
while(idx<no_frm):
    for j in range(0,max_tick):
        min_dist = 10000
        for k in range(0 , max_tick):
            if (data[idx][k] != ' 0') & (data[idx-1][j] != ' 0') & (data[idx][j] != ' 0'):
                dist = euq_distance(data[idx][k],data[idx-1][j])
                #distance[idx-1][j] = dist
                if (dist < min_dist):
                    temp = data[idx][j]
                    data[idx][j] = data[idx][k]
                    data[idx][k] = temp
                    min_dist = dist
    idx = idx + 1
print(data)
#data gets reagranged
################################################################################################################
color = [(255,20,20), (20,255,20), (20,20,255), (255, 255, 255), (34, 67, 19), (255, 255, 255), (56, 88, 199), (3, 46, 200), (33,77,111), (55,200,11), (78,56,19), (88,88,126), (99,99,0), (78,150,7), (3,33,222), (88,72,151)]
for idx in range (0, no_frm):
    c = 0 
    Flag = 0
    image_path = 'Op/Frame%05d.png'%idx
    image_path = os.path.join(current_directory, image_path)
    output_path = 'Anotated/AnotatedFrame%05d.png'%idx
    input_image = Image.open(image_path)
    pixel_map = input_image.load()
    width, height = input_image.size
    wd = int(width/100)
    mid_points = data[idx]
    length = len(mid_points)
    for i in range(length):
        if (mid_points[i] == ' 0'):
            continue
        start = mid_points[i].split()
        if (Flag == 1):
            Flag = 0
            c = c + 1
            continue
        if (i < length-1):
            if(mid_points[i]==mid_points[i+1]):
                Flag = 1
        for j in range(wd):
            for k in range(wd):
                pixel_map[int(float(start[0]))-j,int(float(start[1]))-k] = color[c]
                pixel_map[int(float(start[0]))+j,int(float(start[1]))+k] = color[c]
                pixel_map[int(float(start[0]))-k,int(float(start[1]))+j] = color[c]
                pixel_map[int(float(start[0]))+k,int(float(start[1]))-j] = color[c]
        c = c + 1
    input_image.save(output_path, format="png")
#forming the annotations
################################################################################################################
form(current_directory,os.path.join(current_directory, 'Anotated'))
#compiling the video
################################################################################################################