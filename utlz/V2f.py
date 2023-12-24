import cv2
import os
def video(curr_dir):
    current_directory = curr_dir
    vid_path = os.path.join(current_directory, 'vid/vid2.mp4')
    vid = cv2.VideoCapture(vid_path)
    success,image = vid.read()
    c = 0
    while success:
      cv2.imwrite(os.path.join(current_directory , 'Op/Frame%05d.png' % c), image)
      success,image = vid.read()
      c = c + 1
    print('Break down done to '+str(c)+' frames')
    return c