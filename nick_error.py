a = input("닉네임을 5글자 이내로 입력하세요.")

class NickNameError(Exception):
    pass

def Nick(a):
    if len(a) <= 5:
        b = open("test.txt",'a')
        b.write(a)
        b.close()
        
    else:
        
        raise NickNameError()
    
try:
    Nick(a)
    
except NickNameError:
    print("닉네임이 5글자 이내가 아닙니다.")
    
finally:
    print("처리가 완료되었습니다.")