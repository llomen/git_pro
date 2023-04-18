# -*- coding: utf-8 -*-
import os

import requests
import cv2
import base64
import json
url = "http://10.200.12.73:8080/color_det"

blackbboxs=[]

def diffimages(image_path):
    print('diffimages')
    #if not imp.endswith(".jpg"):continue
    #image_path = os.path.join("samples", imp)
    print('path:',image_path)
    image = cv2.imread(image_path)
    retval, buffer1 = cv2.imencode(".jpg", image)
    image_base64 = base64.b64encode(buffer1).decode()
    
    data = {
        "img":image_base64,
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    data = json.loads(r.text)
    print(data)
    data = parsedata(data)
    if len(data['bboxs'])==0:
        return True,data['bboxs']
    else:
        return False,data['bboxs']
    #print data
    
def parsedata(data):
    
    bboxs = data['bboxs']
    
    for i in bboxs[:]:
        if i in blackbboxs:
            data['bboxs'].remove(i) 
    return data

if __name__ == '__main__':
    path = "/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTest/调试/2-大数据/result/test.png"
    diffimages(path)
    
    
