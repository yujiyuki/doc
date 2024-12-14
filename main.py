import pandas as pd 


df = pd.read_csv('C:\\Users\\otsuy\\OneDrive\\デスクトップ\\sp\\deta.csv')

df['合計'] = df['数学'] + df['国語'] + df['理科']


df.head()

df.to_csv('C:/Users/otsuy/OneDrive/デスクトップ/sp/test0__v2', index=False, encoding='utf-8-sig')
