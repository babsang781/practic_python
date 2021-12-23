now=goal=weeks=cut=0
pct = 25

print('목표 몸무게 관리 프로그램, 달성하면 종료')
now = int(input("현재 몸무게 입력>> "))
goal = int(input("목표 몸무게 입력>> "))

while now>goal :
    weeks +=1
    cut= now/pct
    pct+=15
    print(f'{weeks}주차 감량 몸무게: {round(cut,2)}')
    now -=cut
    
print(f'{round(now,2)} kg 달성!! 축하합니다!')
