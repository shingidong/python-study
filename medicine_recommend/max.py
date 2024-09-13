import streamlit as st

# 사전에 정의된 사용자 정보 딕셔너리
users = {
    "10207": "10207**",
    "10209": "10209**",
    "10214": "10214**",
    "10218": "10218**",
    "10223": "10223**"
}

# 로그인 함수
def login(username, password):
    if username in users:
        if users[username] == password:
            return True, "환영합니다! 로그인에 성공하셨습니다!"
        else:
            return False, "비밀번호가 일치하지 않습니다."
    else:
        return False, "없는 아이디입니다."

# Streamlit 앱 시작
st.title("의약품 추천 시스템")
st.write("by.10218신기동")

# 로그인 상태 변수
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 로그인 화면
if not st.session_state.logged_in:
    st.subheader("로그인")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")
    
    if st.button("로그인"):
        success, message = login(username, password)
        if success:
            st.session_state.logged_in = True
            st.success(message)
        else:
            st.error(message)

# 로그인 후 의약품 추천 시스템
if st.session_state.logged_in:
    st.subheader("의약품 추천 시스템")
    
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