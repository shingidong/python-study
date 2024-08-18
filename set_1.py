배수_2 = set([2,4,6,8,10,12])
배수_3 = set([3,6,9,12,15,18])

print(배수_2 & 배수_3)
print(배수_2 | 배수_3)
print(배수_2 - 배수_3) 

print([i*2 for i in range(10) for j in range(10) if i % 2 == 0])

# a 5 안녕하세요 b 반갑습니다

a = 4

b = "반갑습니다" if a < 5 else "안녕하세요"