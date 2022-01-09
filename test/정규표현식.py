# 참고 링크https://whatisthenext.tistory.com/116 

import re

example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재형, 2019). 또 다른 견해도 있었습니다(Lion, 2018)'
result = re.findall('\([A-Za-z가-힣]*\,\ [0-9]*\)',example)
result

# # findall .. 찾아서 리스트로 값을 반환해줌
result2 = re.findall('[^0-9]*',example)
result2
result3 = re.findall('\([^0-9]*[0-9]*\)',example)
result3
result4 = re.findall('\(\D*\d*\)',example)
result4
result5 = re.findall('\S*',example)
result5
result6 = re.findall('.*',example)
result6


#문자열에서 패턴을 찾을 떄 : re.match( 패턴, 문자열)  : 완전일치 문자 찾기
pattern = r'life' 
script = 'life'
re.match(pattern, script)  # script 에서 패턴 찾기

re.match(pattern, script).group()   # script 에서 ㅐ턴 찾아서 반환하기

def refinder(patter, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a match!')
        
pattern='life'
script = 'Life is so cool'
refinder(pattern,script)
pattern = 'Life'
refinder(pattern,script)
pattern = r'Life'
refinder(pattern,script)
        
