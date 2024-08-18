a = int(input("케이스의 개수를 입력해주새요 : "))
print(a)

for i in range(0,a):
    print("")
    b = int(input(f"{i+1}번째 줄의 케이스의 갯수를 입력해주세요 : "))
    
    if b>=1 and b<=1000:
        c = []
    
    for j in range(0,b):
        c.append(int(input("점수를 입력해주세요 :")))
        
    d = sum(c)
    e = 0
    
    for k in range(0,b):
        if d/b >= c[k]:
            e += 1
            print(100/e)
        



    
    