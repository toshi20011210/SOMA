import os
from PIL import Image
import pyocr
import pyocr.builders
import cv2


#決めないといけない変数ー－－－－－－－－－ー
InputFile = "Tomoki/text.jpg"    #手書き風に変換するファイル名
OutputFile = "Tomoki/putput.png" #保存するファイル名
#ー－－－－－－－－－－－－－－－－－－－－－


#Tesseractの準備（一度きり）ー－－－－－－－
loc_st = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1]
loc_en = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,  2,2,2,2,2,2,3,2,2,3,2,2,2,2,2,3,3,2,2,2,2,2,2,2,3,2]

path_tesseract = "Tomoki/Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

tools = pyocr.get_available_tools()
tool = tools[0]
#ー－－－－－－－－－－－－－－－－－－－－－


#画像のテキストを読み取るー－－－－－－－－－
img = Image.open(InputFile)
results = tool.image_to_string(
    img,
    lang='eng',
    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6)
)
#ー－－－－－－－－－－－－－－－－－－－－－


#座標を補正するー－－－－－－－－－ー－－－－
array = [0]*len(results)
for i in range(0,len(results)):
  array[i] = list(map(list,results[i].position))

time = 0
for box in results:
  
  loc_max = 0
  loc_min = 3

  for i in range(len(box.content)):

    let_num = ord(box.content[i])
    if let_num-65 >= 0 and let_num-65 <= 25:
      let_num -= 55
    elif let_num-97 >= 0 and let_num-97 <= 25:
      let_num -= 61
    else:
      let_num = 10

    if loc_min > loc_st[let_num-10]:
      loc_min = loc_st[let_num-10]
    if loc_max < loc_en[let_num-10]:
      loc_max = loc_en[let_num-10]

  #loc_max = 3
  #loc_min = 0
  if loc_max == 2 and loc_min == 0:
    array[time][1][1] += round((box.position[1][1] - box.position[0][1])/4)
  if loc_max == 3 and loc_min == 1:
    array[time][0][1] -= round((box.position[1][1] - box.position[0][1])/4)
  if loc_max == 2 and loc_min == 1:
    array[time][1][1] += round((box.position[1][1] - box.position[0][1])/2)
    array[time][0][1] -= round((box.position[1][1] - box.position[0][1])/2)
  time += 1
#ー－－－－－－－－－－－－－－－－－－－－－


#元画像に文字を合成して保存するー－－－－－－
time = 0
img = cv2.imread(InputFile)
#height, width = img.shape[:2]

for box in results:

  text_img = cv2.imread('Tomoki/letters\white.png')
  text_img = cv2.resize(text_img,(len(box.content)*26,33))

  for i in range(len(box.content)):
    let_num = ord(box.content[i])

    if let_num-65 >= 0 and let_num-65 <= 25:
      let_num -= 55
      adimg = cv2.imread(f'Tomoki/letters\letter{let_num}.png')
    elif let_num-97 >= 0 and let_num-97 <= 25:
      let_num -= 61
      adimg = cv2.imread(f'Tomoki/letters\letter{let_num}.png')
    else:
      let_num = 10
      adimg = cv2.imread('Tomoki/letters\white.png')
    adimg = adimg[1:27, 1:27]
    adimg = cv2.resize(adimg,(24,(loc_en[let_num-10]-loc_st[let_num-10]-1)*7 + 19))

    x_offset=i*26
    y_offset=loc_st[let_num-10]*7
    text_img[y_offset:y_offset+adimg.shape[0], x_offset:x_offset+adimg.shape[1]] = adimg

  text_img = cv2.resize(text_img,(array[time][1][0]-array[time][0][0]+2,array[time][1][1]-array[time][0][1]+2))
  x_offset=array[time][0][0]-1
  y_offset=array[time][0][1]-1
  img[y_offset:y_offset+text_img.shape[0], x_offset:x_offset+text_img.shape[1]] = text_img
  #cv2.rectangle(img1,(array[time][0][0],array[time][0][1]),(array[time][1][0],array[time][1][1]),(0,0,255))
  time += 1

cv2.imwrite(OutputFile, img)
#ー－－－－－－－－－－－－－－－－－－－－－



img = Image.open(InputFile)
text = tool.image_to_string(
  img,
  lang='eng',
  builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
#builder = pyocr.builders.TextBuilder(tesseract_layout=6)
#text = tool.image_to_string(img, lang="eng", builder=builder)
print(text[9])
