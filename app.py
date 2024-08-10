import streamlit as st

st.title("안녕하세요")

st.write("안녕하세요 계산기니다")

num1 = st.number_input("첫번째 숫자", key="number1", placeholder="계산할 숫자를 입력해주세요")
num2 = st.number_input("두번째 숫자", key="number2", placeholder="계산할 숫자를 입력해주세요")

option = st.selectbox("계산 방식", ("더하기", "빼기", "나누기", "곱하기"), key="option1")

button = st.button("계산")

if button:
    
    if option == "더하기":
        st.write(num1 + num2)
        
    if option == "빼기":
        st.write(num1 - num2)
        
    if option == "곱하기":
        st.write(num1 * num2)
        
    if option == "나누기":
        
        try:
            st.write(num1 / num2)
            
        except ZeroDivisionError:
            st.error("나누는 값이 0입니다.")
            
            
    
    




    