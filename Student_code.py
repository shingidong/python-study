data = {10209:"10209**",10214:"10214**",10218:"10218**",10223:"10223**"}

def login():
    id = input("아이디를 입력해주세요 : ")
    
    for i in range(1,6):
        if id in data.keys():            
            password = input("비밀번호를 입력해주세요 : ")
            
            if password in data.values():                
                print("환영합니다! 로그인에 성공하셨습니다!")                
                break
                
            else:
                print("없는 비밀번호입니다. 다시 입력해주세요.")
                print("기회는",5-i,"회 남았습니다.")
                
        else:
            print("없는 아이디입니다. 다시 입력해주세요.")
            print("기회는",5-i,"회 남았습니다.")
        
        if i == 0:
            print("로그인 횟수를 초과하였습니다.")
            break

def membership():
    while True:
        id = input("회원가입 할 아이디를 입력해주세요(6~10글자) : ")
        
        if len(id)>=6 and len(id)<=10:
            
            password = input("회원가입 할 비밀번호를 입력해주세요(6~10글자) : ")
            
            if id not in data.keys():
            
                if len(password)>=6 and len(password)<=10:
                    
                    print("환영합니다! 회원가입에 성공하셨습니다.")
                    print(f"아이디 :{id},비밀번호 :{password}입니다.")
                    break
                    
                else:
                    print("비밀번호를 6~10글자로 입력해주세요.")
                    
            else:
                print("이미 있는 아이디 입니다. 새로 만들어주세요.")
                
        else:
            print("아이디를 6~10글자로 입력해주세요.")
        
def stop():
    print("프로그램을 종료합니다.")

while True:
    def main():
        try:
            a = int(input("로그인은 1,회원가입은 2, 종료는 3 을 선택해주세요"))
            
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            return
        
        if a == 1:
            login()
            continue
                
        elif a == 2:
            membership()
            continue
            
        elif a == 3:
            stop()
            break
        
        else:
            print("잘못 입력하셨습니다. 다시 입력하세요.")
            continue
            