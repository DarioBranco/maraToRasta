import xml.etree.ElementTree as ET
import json
import glob as g
import os
from pathlib import Path

#eliminate all index.json in each subdir
pathlist = g.glob("C:\\Users\\Dario Branco\\Documents\\Lavoro\\mara2cleo\\BENIIMMOBILI")
for name in pathlist:
    #eliminate all index.json in each subdir
    for subdir in os.listdir(name):
        if(os.path.isdir(name+"/"+subdir)):
            for subsubdir in os.listdir(name+"/"+subdir):
                if(os.path.isdir(name+"/"+subdir+"/"+subsubdir)):
                    jsonpath = name+"/"+subdir+"/index.json"
                    if(os.path.isfile(jsonpath)):
                        os.remove(jsonpath)