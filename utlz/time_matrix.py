import os 
import numpy as np
from utlz.fix import fx
##########################################################################################################
def max_ticking(curr_dir,idx1):
    max_tick = 0
    current_directory = curr_dir
    for i in range(idx1):
        open_path = os.path.join(current_directory,'raw_data/raw_data%05d.txt'%(i))
        file = open(open_path, "r")
        data = fx(file.readline())
        if len(data)>max_tick:
            max_tick = len(data)
        file.close()
    return max_tick
##########################################################################################################
def grt_eqauliser(max_tick, curr_dir, idx1):
    current_directory = curr_dir
    for i in range(idx1):
        open_path = os.path.join(current_directory,'raw_data/raw_data%05d.txt'%(i))
        file = open(open_path, "r")
        data = fx(file.readline())
        lgth = len(data)
        if lgth < max_tick:
            while lgth < max_tick:
                data.insert(len(data), '0')
                lgth =  lgth + 1 
        file = open(open_path, "w")
        L = str(data)
        file.writelines(L)
        file.close()
##########################################################################################################
def time_data(curr_dir):
    tp = os.listdir('./raw_data')
    idx1 = len(tp)
    current_directory = curr_dir
    max_tick = max_ticking(current_directory,idx1)
    print("max tick = "+ str(max_tick))
    grt_eqauliser(max_tick, current_directory, idx1)
    open_path = os.path.join(current_directory,'raw_data/raw_data00000.txt')
    file = open(open_path,"r")
    d = file.readline()
    data = fx(d)
    for i in range(idx1-1):
        open_path = os.path.join(current_directory,'raw_data/raw_data%05d.txt'%(i+1))
        file = open(open_path,"r")
        d = file.readline()
        d = fx(d)
        data = np.vstack((data,d))
    file.close()
    return data , max_tick
##########################################################################################################
def time_test():
    data = time_data()
    data_split = data[0][2].split()
    dataZ = float(data_split[0]) + float(data_split[1])
    print("#"*150)
    print(data)
    print("#"*150)
    print(dataZ)
    print("#"*150)
##########################################################################################################