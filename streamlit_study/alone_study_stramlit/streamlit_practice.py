import streamlit as st
from datetime import time, datetime

st.header('st.slider')#이거 없으면 안 돌아감

st.subheader('Slider')

age = st.slider('당신의 나이는?', 0.00, 130.00, 5.00) #뒤에 5.00는 그냥 초깃값 / ()안에 소수점 단위는 항상 같아야 함
st.write("나는 ", age, '살입니다')

st.subheader('범위 슬라이더')

value = st.slider('값의 범위를 선택하세요', 0.0, 100.0, (25.0, 75.0)) #( (값을 2개를 넣어서 최대,최솟값 기입) )
st.write('값:', value)

st.subheader('시간 범위 슬라이더')

appointment = st.slider( "약속을 예약하세요:",value=(time(11, 30), time(12, 45))) #11,30은 11시 30분
st.write("예약된 시간:", appointment)

st.subheader('날짜 및 시간 슬라이더')

start_time = st.slider( "언제 시작하시겠습니까?",value=datetime(2020, 1, 1, 9, 30),format="MM/DD/YY - hh:mm") #value를 통해 날짜를 입력하고 포멧을 함으로써 년도,월,시간,분,초 를 간편히 확인 가능!
st.write("시작 시간:", start_time)

start_color, end_color = st.select_slider("원하는 색을 선택해주세요",options=["빨강","주황","노랑","초록","파랑","남색","보라"],value=("빨강", "초록"),) 
#앞에 start_color, end_color를 입력하고 뒤에 value값에다 선택권을 입력하면 value에다 2개를 입력하고 빨강~보라 사이로 입력한다.
st.write("너는 색을 ", start_color, "그리고", end_color,"사이로 선택했습니다.")