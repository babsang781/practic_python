# Python Cheat Sheet
<h3>- 내장함수 () 안에 수, 변수, 계산, 리스트 등</h3>
  - sum(), mean(), max(), min(),abs(), pow(x,2)
  - 정렬: sorted(), reversed(), range(0,11,1) 범위 값 생성
  - 형 변환:  str(), tuple(), list(), int()  / type(): 형 확인
  	- int('11',2) -bin>dec ,hex(),bin()-이진수, ord()<->char(): ascii 
	- list(zip([1,2,3],[10,20,30])) >> [(1,20),(2,20),(3,30)]
  - bool()- 0,none, null ->False / all(시퀀스) -시퀀스가 모두 참>True / any(시퀀스) - 시퀀스가 하나라도 참>True
<br/>
<h3>- import random as rd</h3>
  - list1= rd.randrange(1,8)  # 1~7 중의 수
  - rd.shuffle(list1)
  - rd.choice(list1)
  - rd.choice([True,False])
 
<h2>List와 Numpy 배열</h2>
<h3>list 함수와 키워드 - 인덱싱, 슬라이싱 가능</h3>
  - 추가 : insert(index , 값) 와 append(값) 
  - 삭제 : remove(값) , // 삭제 키워드: del list[1]
  - 정렬 : sort(), sort(reverse()=True), reverse()
  - 찾기 종류 : index() 와 count() 와 pop() 와 len()
  - 포함 여부True/False : in ,  not in 

<h3>Numpy Array</h3>
  - python 리스트를 numpy 배열에 넣음:   arr = np.array(list1)  # arr에서 쓰는 확인 함수(저장안됨)
  - 행열 크기: .shape    //  # 전체요소 개수: .size   // # 배열 차원: ndim     
  - reshape(5[행],10[열])    // # 데이터타입: .dtype    // # 데이터 타입 변환 : arrx.astype('int')   [ 소수점 내림]

  - 0~49까지 정수값이 담긴 1차원 배열 생성 :  arr2 = np.arange(50)
  - 1 부터 50까지 50등분한 배열 만들기 np.linspace(1,50,50)
  - 0으로 초기화 하는 것( 원래 임의값 있음?) np.zeros((3,2))  // .ones  .full((3,4),5) 가능
  - 0~1 사이 랜덤 값으로 배열 생성 :  np.random.rand(배열의 크기) [행,열] 형태 
  - [지정한 정수 범위] 2-9사이 정수로 된 3x2랜덤 배열 생성 : np.random.randint(2,10, size=(3,2))

- data = np.loadtxt('ratings.txt', delimiter="::", dtype = 'int')

<h2>Pandas, Series 와 DataFrame</h2>
<h3>Series </h3>
  - series 연산,  추가,  삭제
  - population /1000000         # series 연산 : value 에만 영향을 줌 (사칙연산 가능)
  - population - population2         # 시리즈 끼리의 연산 

<h4>series인덱싱</h4>
  - population[1],  population['부산'] ,  population['부산':'대구']     # series 인덱싱  : 둘 다 가능  , '부산':'대구'는 '대구' 포함결과
  - population[ ['인천', '서울','인천'] ]  , 또는 [ [0,3,1] ]      #  []  리스트 안에 넣음으로서 다중 인덱싱 
  - population[(population<=5000000) & (population>=2500000)]      #boolean 인덱싱
  - ds = population - population2  ->   ds[ds.notnull()]   또는 ds[ds.isnull()]        # null 여부로 인덱싱  

<h4>데이터프레임 정보 확인 </h4>
  - df.index = ['서울', '부산','인천','대구']          # 데이터 프레임을 만든 후에 인덱스 설정
  - 값 , 인덱스 , 컬림  : values , index , columns
  - print(df2.values) , print(df2.index) ,  print(df2.columns) 
	
<h4>데이터 프레임 생성과 전치</h4>
  - data = [ 
    	[9904312, 9631482],
	[3448727, 3393191],
    	[2890451, 6232035],
    	[2466052, 2431774]
	]
	ind = ['서울','부산','인천','대구']      # 직접 입력 가능, 별도 선언 해서 입력도 가능 
	col = ['2015','2010']        
	df3 = pd.DataFrame(data,  index = ind ,  columns = col)       # 별도 선언한 index ,col 이름 대입
	print(df3)

  - df2 = df3.T        # 전치 기능 df.T  // df.transpose() : 이것도 천치, transpose()는 numpy에서도 가능

<h4>데이터프레임 고급 인덱싱: 인덱서</h4>    
  - iloc: 인덱스 번호 / loc: 지정한 인덱스   [index , columns]
  - df2['2005'] = [9762546,3512547,2517680,'dd']          # 각 컬럼이 하나의 시리즈라고 보면 됨. 기본이 컬림 기준:
  - df2['2015']         # 시리즈로 출력
  - df2[['2015']]         # dataframe 으로 출력

  - df2.loc['서울':'부산', '2015':'2010']        # 주로 loc 를 씀
  - df2.loc[df2.loc[:,'2010']>=2500000]     == df2.loc[bol,:]   (bol = df2.loc[:,'2010']>=2500000)   # 불리언 인덱싱 가능, bol행열 구분
