import streamlit as st
import numpy     as np
import pandas    as pd
import matplotlib.pyplot as plt

#タイトル
st.title('デュレーションカーブ')

#"""
# 潮流実績
#"""
#北海道の潮流データ取り込み
data_h = pd.read_csv('2019_hokkaido_transmission2.csv')
#東北の潮流データ取り込み
#data_t = pd.read_csv('streamlit_time_tide_data_t.csv')

time  = []
dummy = []
for i in range(len(data_h)):
    time.append(i)
    dummy.append(0.0)

"""
# 送電線情報:北海道
"""
info_h = pd.read_csv('2019_hokkaido_info.csv')
info_h[1:2].T

#北海道
#セレクトボックス:送電線名の選択
option_h = st.selectbox(
    '北海道エリアについては、Grid_Numberを1〜70の間で指定してください',
    list(range(1,71))
)
'Grid_Name:::', info_h[info_h.columns[option_h]][1], ':::'

# 折れ線グラフ
st.line_chart( data_h[data_h.columns[option_h]][1:8785] )
st.line_chart( sorted(data_h[data_h.columns[option_h]][1:8785].astype(float), reverse=True) )


#セレクトボックス:月の選択
month = st.selectbox(
    '月を1〜12の間で指定してください',
    list(range(1,13))
)
month_h = data_h[data_h.month == month]
year = int( month_h.year[1:2] )
'Grid_Name:::', info_h[info_h.columns[option_h]][1], '::: ', year,'年:::', month, '月:::'

# 折れ線グラフ
st.line_chart( month_h[month_h.columns[option_h]] )
st.line_chart( sorted(month_h[month_h.columns[option_h]].astype(float), reverse=True) )




