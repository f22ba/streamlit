import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#streamlit run main_2.pyをターミナルで実行

st.title('Streamlit2')

st.sidebar.write('Interactive Widgets')
text = st.sidebar.text_input('あなたの趣味は？')
condistion = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text
'コンディション:', condistion

st.write('Display Image')
option = st.selectbox(
    '好きな数字を教えてください、',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

if st.checkbox('Show Image'):
    img = Image.open('Landscape-Color.jpg')
    st.image(img, caption='land', use_column_width=True)


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)