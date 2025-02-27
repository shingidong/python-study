import streamlit as st

# 증상 목록
out_symptoms = ["근육통", "근육피로", "관절통", "삠", "벌레물림", "염증", "찰과상", "화상", "감염", "여드름"]
in_symptoms = ["신체 통증", "소화불량", "속쓰림", "발열", "체", "근육통", "관절염", "감기", "독감", "오한"]

# 외상 증상에 따른 의약품 추천
def recommend_out_symptom(symptom):
    if symptom in ["근육통", "근육피로", "관절통", "삠"]:
        return "환자에게 알맞는 의약품은 파스입니다."
    elif symptom == "벌레물림":
        return "환자에게 알맞는 약은 벌레물림 약입니다."
    elif symptom in ["염증", "찰과상", "화상", "감염", "여드름"]:
        return "환자에게 알맞는 약은 연고입니다."
    else:
        return "잘못된 증상입니다. 다시 입력하세요."

# 내상 증상에 따른 의약품 추천
def recommend_in_symptom(symptom):
    if symptom in ["신체 통증", "근육통", "관절염"]:
        return "환자에게 알맞는 의약품은 진통제입니다."
    elif symptom in ["소화불량", "체"]:
        return "환자에게 알맞는 약은 소화제입니다."
    elif symptom in ["발열", "감기", "독감", "오한"]:
        return "환자에게 알맞는 약은 해열제입니다."
    elif symptom == "속쓰림":
        return "환자에게 알맞는 약은 위장약입니다."
    else:
        return "잘못된 증상입니다. 다시 입력하세요."

# Streamlit 앱 시작
st.title("의약품 추천 시스템")

# 사용자 입력받기
option = st.radio("외상인지 내상인지 혹은 밴드를 원하신다면 '밴드'를 선택하세요:", ["외상", "내상", "밴드"])

# 외상 옵션 처리
if option == "외상":
    symptom = st.selectbox("외상 증상을 선택하세요:", out_symptoms)
    if st.button("의약품 추천"):
        recommendation = recommend_out_symptom(symptom)
        st.write(recommendation)

# 내상 옵션 처리
elif option == "내상":
    symptom = st.selectbox("내상 증상을 선택하세요:", in_symptoms)
    if st.button("의약품 추천"):
        recommendation = recommend_in_symptom(symptom)
        st.write(recommendation)

# 밴드 옵션 처리
elif option == "밴드":
    st.write("밴드를 가져가세요.")