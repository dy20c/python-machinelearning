#넘파이의 기반 데이터 타입은 ndarry => 다차원(Multi-demension) 배열을 쉽게 생성하고 다양한 연산 수행 가능
import numpy as np

#넘파이 array() 함수는 파이썬의 리스트와 같은 다양한 인자를 입력 받아서 ndarray로 변환하는 기능 수행
array1 = np.array([1, 2, 3])
print('array1 type:', type(array1))
print('array1 array 형태:', array1.shape)

array2 = np.array([[1, 2, 3],
                   [2, 3, 4]])
print('array2 type:', type(array2))
print('array2 array 형태:', array2.shape)

array3 = np.array([[1, 2, 3]])
print('array3 type:', type(array3))
print('array3 array 형태:', array3.shape)

print('array1: {:0}차원, array2: {:1}차원, array3: {:2}차원'.format(array1.ndim,
                                                              array2.ndim, array3.ndim))