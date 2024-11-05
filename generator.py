
# 상수

PI = 3.141592

def even_numbers(n):
    i = 0
    
    while i < len(n):
        yield n[i]*n[i]
        i += 1

# Call by Value / Call by Reference

s = [1,3,4,6,23,35,13,14]

for i in even_numbers(s):
    print(i)

# DB why

# DB connect -> commit -> close

# db connect -> cur / 요청 다 처리하고 / yield cur / 함수 다시 한번 호출 / db.close()
