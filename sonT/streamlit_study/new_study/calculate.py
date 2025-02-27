import streamlit as st

st.title("계산기입니다.")

a = st.number_input("첫 번째 수를 입력해주세요 : ")
b = st.number_input("두 번째 수를 입력해주세요 : ")

더하기, 빼기, 곱하기, 나누기 = st.columns(4)


if st.button("더하기"):
    st.write(a+b)

if st.button("빼기"):
    st.write(a-b)

if st.button("곱하기"):
    st.write(a*b)

if st.button("나누기"):
    st.write(a/b)