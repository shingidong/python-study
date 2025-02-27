import streamlit as st

st.title("안녕하세요")

st.write("안녕하세요 칼로리 계산기입니다!")


option = st.selectbox("기초대사량,예상 운동 칼로리 계산,섭취 칼로리 계산을 선택해주세요",("기초대사량", "예상 운동 칼로리","섭취 칼로리"))
st.write("기초대사량,예상 운동 칼로리 계산,섭취 칼로리 계산을 선택해주세요")

if option == "기초대사량":
    
    gender = st.selectbox("성별을 선탹해주세요",("남자","여자"))
    st.write("성별을 선탹해주세요")
    
    Weight = st.number_input("Weight", key="Weight1", placeholder="몸무게를 숫자만 입력해주세요(~kg)")
    Height = st.number_input("Height", key="Height1", placeholder="키를 숫자만 입력해주세요(~cm)")
    Age = st.number_input("Age", key="Age1", placeholder="나이를 숫자만 입력해주세요(~살)")
    
    boy_bmr = 66.47 + (13.75 * Weight) + (5 * Height) - (6.76 * Age)
    girl_bmr = 65.51 + (9.56 * Weight) + (1.85 * Height) - (4.68 * Age)
    
    if gender == "남자":        
        st.write("기초대사량은", boy_bmr ,"kcal입니다.")
        
    if gender == "여자":        
        st.write("기초대사량은", girl_bmr ,"kcal입니다.")

if option == "예상 운동 칼로리":
    
    choice = st.selectbox("운동할 방식을 선택하세요",("수영","달리기","걷기","농구","축구"))
    st.write("운동할 방식을 선택하세요")
    
    Time = st.number_input("Time", key="Time1", placeholder="운동할 시간을 입력해주세요(시간)")
    Level = st.number_input("Level", key="Level1", placeholder="운동할 세기를 선택해주세요(1~5)")
    
    if choice == "수영":
        
        total_cal = Time * (600 + Level * 50)
    
        st.write("예산 칼로리 소모는",total_cal,"입니다")
        
    if choice == "달리기":
        
        
        st.write("예산 칼로리 소모는",Time * (600 + Level * 50),"입니다")
        
    if choice =="걷기":
        
        
        st.write("예산 칼로리 소모는",Time * (300 + Level * 25),"입니다")
        
    if choice == "농구":
       
        
        st.write("예산 칼로리 소모는",Time * (520 + Level * 40),"입니다")
        
    if choice == "축구":
        
        
        st.write("예산 칼로리 소모는",Time * (600 + Level * 50),"입니다")

if option == "섭취 칼로리":
    Calorie = st.number_input("Calorie_Calculate", key="Calorie_Calculate", placeholder="위에서 계산한 기초대사량을 입력해주세요")
    Exercise = st.number_input("Exercise_Calculate", key="Exercise_Calculate", placeholder="위에서 계산한 예상 칼로리 소모량을 입력해주세요")
    Consume = st.number_input("Consume_Calorie", key="Consume_Calorie", placeholder="하루동안 섭취한 총 칼로리를 입력해주세요")
    
    if Consume < 0:
        try:
            Consume = st.number_input("Consume_Calorie", key="Consume_Calorie", placeholder="하루동안 섭취한 총 칼로리를 입력해주세요")
            
        except:
            st.write("섭취한 탈로리를 0 이상으로 입력햐주세요")
            
       
    if Calorie+Exercise-Consume >= 0:
            st.write(Calorie+Exercise-Consume,"만큼 더 섭취해야합니다.")
            
    if Calorie+Exercise-Consume == 0:
            st.write("하루 적정량 섭취하셨습니다.")
            
    if Calorie+Exercise-Consume <= 0:
            st.write(Calorie+Exercise-Consume * -1,"만큼 더 섭취하셨습니다.")