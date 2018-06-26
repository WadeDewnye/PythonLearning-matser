from pandas import Series, DataFrame
from numpy.random import randn
import pandas as pd
import numpy as np
from numpy.linalg import inv, qr

arr1 = randn(6)
# print(np.sort(arr1))
# print(arr1.sort())

arr2 = randn(5, 3)
# print(np.sort(arr2, axis=0))
# print(np.sort(arr2, axis=1))

arr3 = randn(1000)
arr4 = np.sort(arr3)
# print(arr4[int(0.05 * len(arr4))])

names = np.array(['Bob', 'Joe', 'Bob', 'Joy', 'Will', 'Joy'])
# print(names)
# print(np.unique(names))

values = np.array([6, 8, 10, 6, 9, 1, 7])
arr5 = np.intersect1d(values, [2, 3, 4, 7, 9])
# print(arr5)

# 存储一个数组到文件中
arr6 = np.arange(10)
np.save('data1', arr6)

arr7 = np.load('data1.npy')
# print(arr7)

arr8 = np.arange(20)

# 将多个数组,压缩存储在一个文件中,格式npz
np.savez('data3', a=arr6, b=arr7, c= arr8)
arch = np.load('data3.npz')

arr9 = arch['a']
arr10 = arch['b']
arr11 = arch['c']
# print(arr9, arr10, arr11)

arr12 = np.array([[1, 2, 3], [4, 5, 6]])
arr13 = np.array([[1, 2], [3, 4], [5, 6]])
arr14 = np.dot(arr12, arr13)
arr15 = arr13.dot(arr12)

# print(arr14)
# print(arr15)

x = randn(5, 5)
mat = x.T.dot(x)
# print(inv(mat))
print(mat.dot(inv(mat)))



