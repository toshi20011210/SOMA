import streamlit as st
from PIL import Image
import pyocr
import pyocr.builders
import cv2
import os


st.title("英字手書きAI")
#st.text_input('インプットボックス')
file_type = ['jpg', 'png']
input_image = st.file_uploader("ファイルをアップロード", type=file_type)


#image = Image.open('Tomoki/output.png')

if st.button('run'):    
    #st.image(image, caption='サンプル', use_column_width=True)
    #path_tesseract = "C:\\Program Files (x86)\\Tesseract-OCR"

    path_tesseract = "Tesseract-OCR"
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract

    tools = pyocr.get_available_tools()
    tool = tools[0]

#INPUT IMAGE
    img = Image.open(input_image)
    result = tool.image_to_string(
        img,
        lang='eng',
        builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6)
    )

#text go-sei
    img1 = cv2.imread(input_image)

for box in result:

  for i in range(len(box.content)):
    let_num = ord(box.content[i])

    if i == 0:
      if let_num-65 >= 0 and let_num-65 <= 25:
        text_img = cv2.imread(f'Tomoki/letters\letter{let_num-55}.png')
      elif let_num-97 >= 0 and let_num-97 <= 25:
        text_img = cv2.imread(f'Tomoki/letters\letter{let_num-61}.png')
      else:
        text_img = cv2.imread('Tomoki/letters\white.png')
    else:
      if let_num-65 >= 0 and let_num-65 <= 25:
        adimg = cv2.imread(f'Tomoki/letters\letter{let_num-55}.png')
      elif let_num-97 >= 0 and let_num-97 <= 25:
        adimg = cv2.imread(f'Tomoki/letters\letter{let_num-61}.png')
      else:
        adimg = cv2.imread('Tomoki/letters\white.png')
      text_img = cv2.hconcat([text_img, adimg])

    text_img =cv2.resize(text_img,(box.position[1][0]-box.position[0][0]+2,box.position[1][1]-box.position[0][1]+2))
    x_offset=box.position[0][0]-1
    y_offset=box.position[0][1]-1
    img1[y_offset:y_offset+text_img.shape[0], x_offset:x_offset+text_img.shape[1]] = text_img
    #output

    #cv2.imwrite('output.png', img1)

    #st.image(img1, caption='サンプル', use_column_width=True)
    #st.image('img1', caption='アウトプット', width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")
