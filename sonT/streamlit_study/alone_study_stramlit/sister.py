import streamlit as st

# 🦄 웹페이지 설정
st.set_page_config(page_title="누나 멍청이 누나 바보", page_icon="😼", layout="wide")

# 🎨 스타일 적용
st.markdown(
    """
    <style>
        .big-title {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #FF5733;
        }
        .subtitle {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            color: #900C3F;
        }
    </style>
    """, unsafe_allow_html=True
)

# 🏠 메인 화면
st.markdown('<p class="big-title">🐵 누나 멍청이 누나 바보 🐵</p>', unsafe_allow_html=True)
st.subheader("🚆 누나는 나를 두고 서울 귀양갔다.")

st.write(
    """
    누나는 서울로 가서 나를 두고 떠나버렸어.  
    🤖 동생AI를 이용해서 누나의 행동을 분석하고,  
    🔍 그녀의 특징을 파헤쳐보자.
    """
)

# 📌 페이지 탭 만들기
tab1, tab2, tab3, tab4 = st.tabs(["🎭 누나의 특징", "📸 서울 간 누나", "🎨 누나 갤러리", "📢 추모글"])

# 🎭 누나의 특징
with tab1:
    st.header("🎭 누나의 특징")
    
    st.markdown("""
    🐵 **누나의 장점**
    - 🧠 가끔 멍청함
    - 🎨 인스타 감성 충만
    - 🏃‍♀️ 서울에서 문화생활 즐김  

    🐛 **누나의 단점**
    - 🤳 하루 종일 인스타함
    - 🎤 틱톡 챌린지 찍음
    """)

# 📸 서울 간 누나
with tab2:
    st.header("📸 서울 간 누나의 일상")
    
    st.write("🔍 **서울 간 누나는 이런 짓을 하고 있다...**")
    
    activities = [
        "☕ 미팅",
        "💄 클럽 가기",
        "🎤 노래방에서 고음 도전",
        "📸 인스타 스토리 업로드",
        "🍕 새벽에 배달음식 시킴"
    ]
    
    for act in activities:
        st.write(f"✅ {act}")

# 🎨 누나 갤러리
with tab3:
    st.header("🎨 누나 갤러리")
    st.write("🐵 누나의 ㄹㅈㄷ 순간을 감상하자!")
    
    uploaded_files = st.file_uploader("📷 누나의 레전드 사진 업로드", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
    
    if uploaded_files:
        for img in uploaded_files:
            st.image(img, use_column_width=True)

# 📢 누나 헌정글
with tab4:
    st.header("📢 누나에게 보내는 추모글")
    
    user_message = st.text_area("💌 누나에게 하고 싶은 말을 남겨보세요!", "")
    
    if st.button("💌 메시지 전송"):
        st.success("🚀 메시지가 전송되었습니다!")

# 하단 푸터
st.markdown("---")
st.write("© 2025 누나 멍청이 누나 바보 | 제작자: 세상에서 가장 쩌는 동생 😼")