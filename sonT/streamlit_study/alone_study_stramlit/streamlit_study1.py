import streamlit as st
import pandas as pd
import numpy as np


#st.line_chart는 라인 차트를 표시

#st.altair_chart 구문를 단순화, 데이터의 열과 인덱스를 활용해 차트 명세를 결정한다는 점에서 차이. 그 결과로 ‘데이터를 차트로 간단히 표현’하는 많은 상황에서 사용하기 편리, 사용자가 자세히 설정하기는 어려움.
# 따라서 st.line_chart가 데이터 명세를 정확히 예측하지 못하는 경우에는 st.altair_chart를 사용해 원하는 차트를 명시적으로 지정.

st.header('라인 차트')

chart_data = pd.DataFrame( np.random.randn(20, 3),columns=['a', 'b', 'c'])
st.line_chart(chart_data)