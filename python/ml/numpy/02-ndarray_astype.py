import numpy as np

#ndarray 내 데이터 값의 타입 변경도 astype() 메서드 이용해서 가능
#astype()에 인자로 원하는 타입을 문자열로 지정
#데이터 타입을 변경하는 경우는 대용량 데이터의 ndarray를 만들 때 많은 메모리가 사용되는데, 메모리 더 절약해야할 때 보통 이용
#가령 int형으로 충분한 경우인데, 데이터 타입이 float이라면 int 형으로 바꿔 메모리 절약

array_int = np.array([1, 2, 3])
array_float = array_int.astype('float64')
print(array_float, array_float.dtype)

array_int1 = array_float.astype('int32')
print(array_int1, array_int1.dtype)

array_float1 = np.array([1.1, 2.1, 3.1])
array_int2 = array_float1.astype('int32')
print(array_int2, array_int2.dtype)
