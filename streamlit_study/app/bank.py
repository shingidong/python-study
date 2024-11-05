import streamlit as st

# Session State를 초기화하는 함수
def initialize_session_state():
    if 'exchange_rates' not in st.session_state:
        st.session_state.exchange_rates = {
            'USD': 1.0,    # 기본 통화는 USD
            'EUR': 0.85,   # 유로
            'JPY': 110.0,  # 일본 엔
            'KRW': 1200.0, # 한국 원화
        }
    if 'balance' not in st.session_state:
        st.write("초기 잔액 : ") # TODO: 초기 잔액 설정 (1000 USD) 
        st.session_state.balance = '1000 USD'  # TODO: 여기에 초기 잔액을 설정하세요

# 환율 데이터를 업데이트하는 함수
def update_exchange_rate(currency, rate):
    if currency in st.session_state.exchange_rates:
        st.session_state.exchange_rates[currency]= rate
        pass  # TODO: 여기에 환율 데이터를 업데이트하는 코드를 작성하세요
    else:
        # TODO: 새로운 통화를 추가하기
        pass  # TODO: 여기에 새로운 통화를 추가하는 코드를 작성하세요

# 환전 계산을 수행하는 함수
def calculate_exchange(amount, target_currency):
    if target_currency not in st.session_state.exchange_rates:
        st.error(f"{target_currency} 통화에 대한 환율 데이터를 찾을 수 없습니다.")
        return None
    else:
        exchange = amount * target_currency
    # TODO: 환전 결과 계산하기 o
    return exchange  # TODO: 여기에 환전 계산 결과를 반환하세요 o

# 입금 함수
def deposit(amount):
    
    # TODO: 입금 금액을 현재 잔액에 추가하기
    pass  # TODO: 여기에 입금 기능을 구현하세요

# 출금 함수
def withdraw(amount):
    if amount > st.session_state.balance:
        # TODO: 잔액 부족 오류 메시지 표시
        pass  # TODO: 여기에 잔액 부족 시 오류 메시지를 표시하세요
    else:
        # TODO: 출금 금액을 현재 잔액에서 차감하기
        pass  # TODO: 여기에 출금 기능을 구현하세요

# 메인 함수: Streamlit 애플리케이션
def main():
    st.title("고급 은행 사이트 (입출금 기능 포함)")

    # Session State 초기화
    initialize_session_state()

    # 현재 잔액 표시
    st.header("현재 잔액")
    st.write(f"${st.session_state.balance} USD")

    # 입출금 기능 UI
    st.header("입출금 기능")
    deposit_amount = st.number_input("입금할 금액 (USD)", min_value=0.0, value=0.0)
    if st.button("입금"):
        # TODO: 입금 함수 호출
        pass  # TODO: 여기에 입금 함수 호출 코드를 작성하세요

    withdraw_amount = st.number_input("출금할 금액 (USD)", min_value=0.0, value=0.0)
    if st.button("출금"):
        # TODO: 출금 함수 호출
        pass  # TODO: 여기에 출금 함수 호출 코드를 작성하세요

    # 환전 기능 UI
    st.header("환전하기")
    amount = st.number_input("환전할 금액 (USD 기준)", min_value=0.0, value=100.0)
    target_currency = st.selectbox("환전할 통화 선택", list(st.session_state.exchange_rates.keys()))

    if st.button("환전 계산하기"):
        # TODO: 환전 계산 함수 호출 및 결과 표시
        converted_amount = None  # TODO: 여기에 환전 계산 함수 호출 결과를 할당하세요
        if converted_amount is not None:
            st.success(f"환전 결과: {amount} USD = {converted_amount} {target_currency}")

    # 환율 관리 기능 UI
    st.header("환율 관리")
    with st.form(key="update_rate_form"):
        currency = st.text_input("통화 코드 입력 (예: EUR, JPY, KRW 등)").upper()
        rate = st.number_input("해당 통화의 환율 입력 (USD 대비)", min_value=0.0, value=1.0)
        update_button = st.form_submit_button("환율 업데이트")

        if update_button and currency:
            # TODO: 환율 업데이트 함수 호출
            pass  # TODO: 여기에 환율 업데이트 함수 호출 코드를 작성하세요

    # 추가 기능: 현재 환율 정보 제공
    st.header("현재 환율 정보")
    for currency, rate in st.session_state.exchange_rates.items():
        st.write(f"1 USD = {rate} {currency}")

if __name__ == "__main__":
    main()
