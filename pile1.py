try:
    print (4/0)
except Exception as e:
    print(e)
    print(4/0)
    print("그런거 계산 못합니다.")
finally:
    print("나 실행됨")