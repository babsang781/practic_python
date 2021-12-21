# 오늘은 12월 21일 입니다.

day = 22
s= '오늘은 12월 %d일 입니다.'%day
print(s)
# 성공

day = 21
s= '오늘은 12월 {}일 입니다.'.format(day)
print(s)
#성공

month = 11
day = 23
s= '오늘은 {}월 {}일 입니다.'.format(month,day)
print(s)
#성공!

month = 12
day = 21
s= '오늘은 %d1월 %d2일 입니다.'%(month,day)
print(s)

x, y , sum2= 100, 200, x+y 
print(x)
print(y)
print(sum2)

print('{}와 {}의 합은 {} 입니다.'.format(x,y,x+y))
print('%d와 %d의 합은 %d 입니다.'%(x,y,sum2))
