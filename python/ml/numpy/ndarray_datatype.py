import numpy as np

#ndarray내의 데이터값은 숫자 값, 문자열 값, 불 값 모두 가능.
#숫자형 int(8bit, 16bit, 32bit) , unsigned int형(8bit, 16bait, 32bit), float형(16bit, 32bit ,64bit, 128bit) -> 이보다 더 큰 숫잢이나 정밀도를 위해 complex 타입도 제공

#리스트 자료형인 list1은 integer 숫자인 1,2,3을 값으로 가지고, ndarray로 쉽게 변경 가능
list1 = [1, 2, 3]
print(type(list1))

#ndarray 내의 데이터값은 모두 int32
array1 = np.array(list1)
print(type(array1))

print(array1, array1.dtype)

print('====================')

list2 = [1, 2, 'test']
array2 = np.array(list2)
print(array2, array2.dtype)

print('====================')

list3 = [1, 2, 3.0]
array3 = np.array(list3)
print(array3, array3.dtype)