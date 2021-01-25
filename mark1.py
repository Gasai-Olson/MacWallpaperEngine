import cv2
import os
from appscript import app, mactypes
import time
import re

def getframes():
    videofile='test.mp4'
    vidcap=cv2.VideoCapture(videofile)
    #get framerate
    vidcap.get(30)
    #create image folder if folder does not exist
    if not os.path.exists('Wallpaper_frames'):
        os.makedirs('Wallpaper_frames')
        direct = 'Wallpaper_frames'
    else:
        name = input('choose a name for this wallpaper')
        direct = name
        os.makedirs(direct)
    x=0
    while(vidcap.isOpened()):
        frameId = vidcap.get(1)#current frame num
        ret, frame = vidcap.read()
        if (ret != True):
            break

        filename = './' + direct + '/frame' + str(int(x)) + '.jpg'
        x+=1
        cv2.imwrite(filename, frame)
        
    vidcap.release()
    print('done')
    cv2.destroyAllWindows()
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def animate(folder):
    l = list()
    a = list()
    for filename in os.listdir(folder):
        path = (os.path.join(folder, filename))
        if path.endswith('jpg'):
            l.append(path)
    f = sorted(l)
    f = list(dict.fromkeys(f))
    f.sort(key=natural_keys)

    while True:
        for ele in f:
                print(ele)
                app('Finder').desktop_picture.set(mactypes.File(ele))
                time.sleep(.001)
    
def fps(video):
    video = cv2.VideoCapture(video)
    fps = video.get(cv2.CAP_PROP_FPS)
    return fps
