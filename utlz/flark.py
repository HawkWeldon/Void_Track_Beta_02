import cv2
import pandas as pd
##################################################################################################################################################
def darknet(results):
    df_list = pd.DataFrame()
    df_list['x_centre'] = (results.pandas().xyxy[0]['xmin'] + results.pandas().xyxy[0]['xmax']) / 2
    df_list['y_centre'] = (results.pandas().xyxy[0]['ymin'] + results.pandas().xyxy[0]['ymax']) / 2
    return df_list
##################################################################################################################################################
def main(image_path,model):
    #inital current directory location 
    input_image = cv2.imread(image_path)[..., ::-1]
    #inital model placement
    results = model(input_image)
    df = darknet(results)
    df = df.to_string(header=False, index=False)
    return df
##################################################################################################################################################