import xml.etree.ElementTree as ET
import json
import glob as g
import os
from pathlib import Path

pathlist = g.glob("C:\\Users\\Dario Branco\\Documents\\Lavoro\\mara2cleo\\DIANA TIFATINA_S. ANGELO IN FORMIS-20230228T080722Z-001\\test")

for name in pathlist:
    for subdir in os.listdir(name):
        num = -1
        if(os.path.isdir(name+"/"+subdir)):
            for subsubdir in os.listdir(name+"/"+subdir):
                if(os.path.isdir(name+"/"+subdir+"/"+subsubdir)):
                    num +=1
                    jsonpath = name+"/"+subdir+"/index.json"
                    item = []
                    x = []
                    y = []
                    btx = []
                    bty = []
                    ant = []
                    width = []
                    heigh = []
                    rdfsource = g.glob(name+"/"+subdir+"/"+subsubdir+"/*.irdf")
                    
                    if(rdfsource != []):
                        tree = ET.parse(rdfsource[0])
                        descriptioniter = tree.getroot().iter("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description")
                        descriptionlist = list(descriptioniter)
                        print(rdfsource)
                        for child in descriptionlist:
                            x.append(child.find(
                                "{http://www.dcs.shef.ac.uk/~ajay/image/annotation#}topX").text)
                            y.append(child.find(
                                '{http://www.dcs.shef.ac.uk/~ajay/image/annotation#}topY').text)
                            btx.append(child.find(
                                '{http://www.dcs.shef.ac.uk/~ajay/image/annotation#}botomX').text)
                            bty.append(child.find(
                                '{http://www.dcs.shef.ac.uk/~ajay/image/annotation#}bottomY').text)
                            ant.append(child.find(
                                '{http://www.dcs.shef.ac.uk/~ajay/image/annotation#}annotationText').text)
                        
                        for i, j in enumerate(x):
                            width.append(str(int(btx[i])-int(j)))

                        for i, j in enumerate(y):
                            heigh.append(str(int(bty[i])-int(j)))

                        with open(jsonpath, "r") as read:
                            data = json.load(read)
                        
                        for i, insert in enumerate(x):
                            target = str(data["items"][num]["id"])+"#xywh=" + insert + "," + y[i] + "," + width[i] + "," + heigh[i]
                            id = str(data["items"][num]["id"])+"/annotation/" + \
                                str(i)+"-tag"
                            item.append({
                                "id": id,
                                "type": "Annotation",
                                "motivation": "tagging",
                                "body": {
                                    "type": "TextualBody",
                                    "value": ant[i],
                                    "language": "it",
                                    "format": "text/plain"
                                    },
                                "target": target
                                })
                        
                        if ("annotations" in data["items"][num]):
                            data["items"][num]["annotations"]["items"] = item
                        else:
                            data["items"][num]["annotations"] = {}
                            data["items"][num]["annotations"]["id"] = "http://192.168.1.3:8087/summerschool"+subdir+"/index.json/canvas/"+str(num)+"/annotationpage/" + \
                                str(num+1)
                            data["items"][num]["annotations"]["type"] = "AnnotationPage"
                            data["items"][num]["annotations"]["items"] = item
                        print(data)
                        json.dumps(data)
                        with open(jsonpath, "w") as f:
                            json.dump(data, f, indent=2)

# Path: BENIIMMOBILI\script.py