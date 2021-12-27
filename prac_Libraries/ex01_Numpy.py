# import 하기, np로 쓰기
import numpy as np


# 1 차원 Array 생성하기 
list1 = [1,2,3,4,5]     # 리스트 생성한 뒤에 np에 넣기
arr = np.array(list1)
 
print(arr)              # 이 array는 다른 점이 없고, 오히려 분석을 위해 다양한 형태의 밸류를 막음
# 리스트 생성과 동시에 np 에 넣기
arr1 = np.array([1,2,3,4,5])
print(arr1)

list1=[1,2,3]
list2=[4,5,6]
list3=[]
for i in range(0,3):
    list3.append(list1[i] + list2[i])
print(list3)

# 2차원 array 생성하기
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#array의 크기 확인하기
# shape 
print(arr2.shape)

# 3 차원의 array 만들고 배열의 크기, 차원 , 전체 요소 개수 확인
# 배열의 크기: shape
# 배열의 차원: ndim
# 배열의 개수: size

arr3 = np.array( [[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr3)

print('배열의 크기 :',arr3.shape)
print(f'배열의 차원 : {arr3.ndim}')
print('배열의 개수 : {}'.format(arr3.size))



