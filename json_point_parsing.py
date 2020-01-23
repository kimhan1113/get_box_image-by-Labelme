import json
import cv2
import numpy as np
from PIL import Image
import os

images = os.listdir('4') # 이미지 폴더
annotation = os.listdir('Annotation') # json 폴더

for i in range(len(images)):

    count = 0 # 이미지 이름 겹치지 않게
    
    try:

        with open(os.path.join('Annotation',os.path.splitext(images[i])[0]+'.json')) as json_file:

            json_data = json.load(json_file)
            shapes = (json_data['shapes'])
            json_name = os.path.splitext(images[i])[0]

            if not os.path.exists(json_name):
                os.mkdir(json_name)

            img = Image.open(os.path.join('4', images[i])) # 이미지 읽기

            for e in shapes: # bounding box parsing
                points = e['points'] #좌표 경로
                po = sum(points, []) # 2차원을 1차원으로
                region = img.crop(po)
                region.save(os.path.join(json_name, str(count) + '.jpg')) #이미지 저장(해당이미지 이름을 폴더로 하여 거기에 bounding box를 전부 이미지로 저장하기)
                count += 1

        print() # 구분하기 위해 일부로 추가
    except: # json이 없을 수 있으니 try, except 으로 오류안나도록 함
        continue
