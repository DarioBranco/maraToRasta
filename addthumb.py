import xml.etree.ElementTree as ET
import json
import glob as g
import os
from pathlib import Path


pathlist = g.glob("C:\\Users\\Dario Branco\\Documents\\Lavoro\\mara2cleo\\DIANA TIFATINA_S. ANGELO IN FORMIS-20230228T080722Z-001\\test")

for name in pathlist:
    for subdir in os.listdir(name):
        num = -1
        print(subdir)
        if(os.path.isdir(name+"/"+subdir)):
            print(subdir)

            for subsubdir in os.listdir(name+"/"+subdir):


                if(os.path.isdir(name+"/"+subdir+"/"+subsubdir)):
                    num +=1
                    jsonpath = name+"/"+subdir+"/index.json"
                    with open(jsonpath, "r") as read:
                        data = json.load(read)
                    if(data["items"][num]["items"][0]["items"][0]["body"]["id"].endswith(".mp4")):
                        items = []
                        name2 = "http://cosme.unicampania.it/rasta/tifantina/"+subdir+"/"+subsubdir+"/default.jpg"
                        items.append({"id" : name2, "type" : "Image"})
                        data["items"][num]["thumbnail"] = items
                        json.dumps(data)
                        with open(jsonpath+'test', "w") as f:
                            json.dump(data, f, indent=2)
