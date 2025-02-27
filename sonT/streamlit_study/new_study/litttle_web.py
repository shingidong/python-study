import streamlit as st

st.title("리틀 웹사이트")

users = {'dave' : 'dave**'}

버튼, 로그인하기, 회원가입 = st.columns(3)

st.button("로그인")
st.button("회원가입")

b = 0
c = 0
id = st.text_input("아이디를 입력해주세요 : ")
password = st.text_input("비밀번호를 입략해주세요 : ")
    
if st.button("로그인하기"):
    if id in users:
            
        if password == users[id]:
            st.write("오랜만이네요 :)")
            
        else:
            c =+ 1
            st.error(f"비번 오류 :( {5-c}번 기회 남음")
            
            if c >= 5:
                st.write("5번 틀림 :(")
            
    else:
        b =+ 1
        st.error(f"아이디 오류 :( {5-b}번 기회 남음")
        
        if b >= 5:
            st.write("5번 틀림 :(")
                

