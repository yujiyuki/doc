import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image as ig
import time


st.title('すくれいぴんぐ')


st.write('dataFrame')

#df = pd.DataFrame(
     
     #   np.random.rand(100,2) /[50,50] +[35.69,139.70],
   #     columns=['lat','lon']   
   #  )
#st.table(df.style.highlight_max(axis=0))  #←dataframeを使うと縦横を決めることができる(highlight_max(axis=0)で色付けも可能)　すげッ！！ table を使うと整列ができないテーブルが出来上がる。


#st.map(df)



#if st.checkbox('表示'):
 #   img = ig.open('hq720.webp')
  #  st.image(img, caption = 'kkkkkk' )


#option = st.selectbox(
 #   '数字を',
  #  list(range(1,11))
#)

#'あんたさんが選んだ数字は',option , 'だ！'

#nn =st.slider('何％？？',0,100,50) #←　３つの数字は、最大値と最小値をさす
#'元気',nn,'%'


#werite = st.text_input('何かを書いてみて') #←表示させるために何か表示分を書かなくても表示させれる　（え,ウィジェット最高）
#werite






st.write('プログレスバー')



letast_iteration = st.empty()
bar = st.progress(60)

for i in range(100):
    letast_iteration.text(f'install {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
    
    
    
    
    

left_column, right_column = st.columns(2)
btn =left_column.button('右ネジ')
if  btn :
    right_column.write('右ネジの法則')


ex = st.expander('Q&A')
ex.write('おバカの相手をしないといけないのだが')
    