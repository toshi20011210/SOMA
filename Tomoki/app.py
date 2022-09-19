from PIL import Image
import numpy as np
import streamlit as st

st.title("hello")
st.button('ボタン')
st.selectbox('コンボボックス',('選択1','選択2'))
st.checkbox('チェックボックス')
st.radio('ラジオボタン',('ラジオボタン1','ラジオボタン2'))
st.date_input('日付インプット')
st.text_input('インプットボックス')
st.text_area('テキストエリア')
st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3")) 
st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3"))

st.file_uploader("ファイルをアップロード", type='jpg')

image = Image.open('Tomoki/output.png')
st.image(image, caption='サンプル',use_column_width=True)


