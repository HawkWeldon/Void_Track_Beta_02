import cv2
import os
import moviepy.editor as mvp
def form(current_directory,image_folder):
    video_name = os.path.join(current_directory, 'temp.avi')
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 10, (width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()
    clip=mvp.VideoFileClip(os.path.join(current_directory, 'temp.avi'));
    clip.write_videofile(os.path.join(current_directory, 'Tracked.mp4'));
    os.remove(os.path.join(current_directory, 'temp.avi'))