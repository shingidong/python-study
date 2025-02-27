import streamlit as st

# 웹페이지 설정
st.set_page_config(page_title="대신고 액트 동아리", page_icon="🔥", layout="wide")

# 메인 화면
st.title("🔥 대신고 액트 동아리")
st.subheader("창의적 사고와 도전 정신을 키우는 최고의 동아리!")

st.write(
    """
    **ACT 동아리는?**
    
    🚀 창의적 사고를 바탕으로 다양한 프로젝트를 수행하는 동아리입니다.  
    🎯 AI, 웹 개발, 공학 프로젝트, 창업 등 다양한 분야에 도전하며 성장합니다.  
    📢 열정 넘치는 학생들이 모여 협업하며 배우는 최고의 동아리입니다!
    """
)

# 📌 페이지 탭 만들기
tab1, tab2, tab3, tab4 = st.tabs(["🏆 동아리 활동", "📸 갤러리", "📢 모집 안내", "📞 연락처"])

# 🏆 동아리 활동 소개
with tab1:
    st.header("🏆 우리 동아리 활동")
    st.write("우리는 다양한 분야에서 프로젝트를 진행하며, 아래와 같은 성과를 이루었습니다.")
    
    st.subheader("🎯 주요 프로젝트")
    st.markdown("""
    - **AI 보도블럭 손상 감지 프로젝트** (90% 정확도)
    - **웹 기반 치매 조기 진단 시스템** (필기 데이터 분석)
    - **학교 생활 편리 앱 개발** (학생들을 위한 앱 제작)
    - **창업 아이디어 공모전 참가 및 수상** 🎖
    """)

    st.subheader("📢 공모전 및 대회 참가")
    st.markdown("""
    - 2024 교육부 창업 공모전 **우수상** 🏅
    - AI 해커톤 **본선 진출** 🚀
    - 정보올림피아드 참가 및 수상
    """)

# 📸 갤러리
with tab2:
    st.header("📸 동아리 활동 갤러리")
    st.write("동아리 활동 중 찍은 사진들을 공유합니다.")
    
    uploaded_files = st.file_uploader("사진 업로드", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
    
    if uploaded_files:
        for img in uploaded_files:
            st.image(img, use_column_width=True)

# 📢 모집 안내
with tab3:
    st.header("📢 동아리 신입 모집 안내")
    
    st.markdown("""
    🏫 **모집 대상**: 대신고 1~2학년 학생  
    📅 **모집 기간**: 매년 3월  
    📌 **지원 방법**: 아래 링크에서 지원서를 작성해주세요.  
    👉 [**지원서 작성하기**](https://forms.google.com)
    """)

# 📞 연락처
with tab4:
    st.header("📞 동아리 문의")
    st.write("궁금한 점이 있으면 언제든지 연락하세요!")

    st.markdown("""
    📩 **이메일**: actclub@school.ac.kr  
    📱 **인스타그램**: [@actclub_official](https://instagram.com)  
    """)

# 하단 푸터
st.markdown("---")
st.write("© 2025 대신고 액트 동아리 | 최고의 창의적 동아리 🌟")