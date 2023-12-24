import os 
def raw(Pn, raw_path):
    L = str(Pn)
    data_path = raw_path
    file = open(data_path, "w")
    file.writelines(L)