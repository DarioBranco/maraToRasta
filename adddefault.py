import os
import glob as g
import shutil
from pyffmpeg import FFmpeg
import requests 
import ffmpeg
import sys
from moviepy.editor import * # import everythings (variables, classes, methods...) inside moviepy.editor
from PIL import Image

def search_file(start_dir, target_file):
    for root, dirs, files in os.walk(start_dir):
        if target_file in files:
            return os.path.join(root, target_file)
    return None


pathlist = g.glob("C:\\Users\\Dario Branco\\Documents\\Lavoro\\mara2cleo\\DIANA TIFATINA_S. ANGELO IN FORMIS-20230228T080722Z-001\\test")


for name in pathlist:
    for subdir in os.listdir(name):
        num = -1
        if(os.path.isdir(name+"/"+subdir)):
            for subsubdir in os.listdir(name+"/"+subdir):
                if(os.path.isdir(name+"/"+subdir+"/"+subsubdir)):
                    found = 1
                    for file in os.listdir(name+"/"+subdir+"/"+subsubdir):

                        if(file.endswith('jpg') and file != "thumb.jpg"):
                            #create a directory for each jpg
                            #create directory if not exists
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles")
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles/full"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles/full")
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120")
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0")
                            #copy img in the new directory
                            shutil.copyfile(name+"/"+subdir+"/"+subsubdir+"/thumb.jpg", name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0/"+file)
                            #rename new img in default.jpg
                            try:
                                os.rename(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0/"+file, name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0/default.jpg")
                            except:
                                None
                            found = 0
                    for file in os.listdir(name+"/"+subdir+"/"+subsubdir):
                        if(file.endswith('mp4') and file != "thumb.jpg" and found == 1):
                            #create a directory for each jpg
                            #create directory if not exists
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles")
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles/full"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles/full")
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120")
                            if not os.path.exists(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0"):
                                os.mkdir(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0")

                            clip = VideoFileClip(name+"/"+subdir+"/"+subsubdir+"/"+file)

                            fbs = clip.reader.fps # return number of frame per second
                            nframes = clip.reader.nframes # return number of frame in the video
                            duration = clip.duration # return duration of the video in second
                            max_duration = int(clip.duration) + 1 
                            frame_at_second = 3 # here is the time where you want to take the thumbnail at second, it should be smaller than max_duration
                            frame = clip.get_frame(frame_at_second) # Gets a numpy array representing the RGB picture of the clip at time frame_at_second 
                            new_image_filepath = os.path.join(name+"/"+subdir+"/"+subsubdir+"/+tiles/full/,120/0/",f"{frame_at_second}.jpg")
                            new_image = Image.fromarray(frame) # convert numpy array to image
                            new_image.save(new_image_filepath) # save the image 
                            new_image = new_image.resize((500, 500))
                            os.rename(new_image_filepath, name+"/"+subdir+"/"+subsubdir+"/default.jpg")




