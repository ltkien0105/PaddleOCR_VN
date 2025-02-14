import json
import os
import cv2
import copy
import numpy as np
from tools.infer.utility import get_rotate_crop_image

type_file = 'unseen'

def print_draw_crop_rec_res( img_crop_list, img_name):
        bbox_num = len(img_crop_list)
        for bno in range(bbox_num):
          crop_name = img_name + '_' + str(bno) + '.jpg'
          crop_name_w = f"train_data/vietnamese/img_crop/{type_file}/{crop_name}"
          cv2.imwrite(crop_name_w, img_crop_list[bno])
          crop_label.write(f"{crop_name}\t{text[bno]}\n")

crop_label = open(f'train_data/vietnamese/img_crop/crop_label_{type_file}.txt','a', encoding='utf-8')
with open(f'train_data/vietnamese/{type_file}_label.txt','r', encoding='utf-8') as file_text:
  img_files=file_text.readlines()
  
count=0

for img_file in img_files:
  content = json.loads(img_file.split('\t')[1].strip())

  dt_boxes=[]
  text=[]
  
  for i in content:
    content = i['points']
    if i['transcription'] == "###":
      count+=1
      continue
    bb = np.array(i['points'],dtype=np.float32)
    dt_boxes.append(bb)
    text.append(i['transcription'])

  image_file = f'train_data/vietnamese/{type_file}_images/' + img_file.split('\t')[0]
  img = cv2.imread(image_file)
  ori_im=img.copy()
  img_crop_list=[]

  for bno in range(len(dt_boxes)):
    tmp_box = copy.deepcopy(dt_boxes[bno])
    img_crop = get_rotate_crop_image(ori_im, tmp_box)
    img_crop_list.append(img_crop)
  img_name = img_file.split('\t')[0].split('.')[0]

  if not os.path.exists(f'train_data/vietnamese/img_crop/{type_file}'):
    os.mkdir(f'train_data/vietnamese/img_crop/{type_file}') 
  print_draw_crop_rec_res(img_crop_list,img_name)

