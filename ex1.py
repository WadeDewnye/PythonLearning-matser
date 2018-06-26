import pytz
from datetime import datetime
import pandas as pd
from dateutil.parser import parse
from pandas import Series, DataFrame
from numpy.random import randn
import pandas as pd
import numpy as np
from pandas.tseries.offsets import Hour,Minute,MonthEnd,Day

ts1 = Series(np.random.rand(3), index=pd.date_range('2010-01-09', periods=3, freq='W-WED'))
# print(ts1)
# print(ts1.resample('B',))

# print(np.ones((10, 2)).shape)
# print(np.ones((3, 5, 4)).strides)

arr = np.arange(10)
# print(arr)
# print(np.add.reduce(arr))

arr1 = randn(5, 5)

df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'c'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                'data1': randn(5),
                'data2': randn(5)})
# print(df)
grouped1 = df['data1'].groupby(df['key1'])
grouped2 = df['data2'].groupby(df['key2'])

# print(grouped1.mean())
#
# print(grouped2.max())
# print(grouped2.min())

means = df['data1'].groupby([df['key1'], df['key2']]).mean()
# print(means)
# print(means.unstack())

states = ['Ohio', 'Califorlia', 'Califorlia', 'Ohio', 'Ohio']
years = [2010, 2011, 2012, 2012, 2013]
means1 = df['data2'].groupby([states, years]).mean()
# print(means1)

means2 = df.groupby('key1').mean()
# print(means2)
means3 = df.groupby(['key1', 'key2']).mean()
# print(means3)

size1 = df.groupby([states]).size()
# print(size1)

# for name, group in df.groupby('key1'):
    # print(name, group)
    # print(group)

# for (k1, k2), group in df.groupby(['key1', 'key2']):
#     print(k1, k2)
#     print(group)

pieces = dict(list(df.groupby('key1')))
# print(pieces['a'])

grouped3 = df.groupby(df.dtypes, axis=1)
# print(dict(list(grouped3)))

means4 = df.groupby(['key1', 'key2'])[['data1']].mean()
# print(means4)

means5 = df.groupby(['key1'])['data1'].mean()
# print(means5)

means = dict(list(df.groupby('key1')))
# print(means)

arr3 = np.arange(15)
# print(arr3)

arr = np.array([1, 2, 3, 4, 5], dtype=np.int8)
# print(arr)

arr4 = np.array([1, 2, 3])
# print(arr4)

# 矢量化:数组,不用循环即可对数据执行运算
# 数组和标量之间的运算

arr5 = np.array([[[1, 2, 3],[4, 5, 6], [7, 8, 9]],
                 [[9, 8, 7],[6, 5, 4], [3, 2, 1]],
                 [[1, 2, 3],[4, 5, 6], [7, 8, 9]],
                 [[9, 8, 7],[6, 5, 4], [3, 2, 1]]])
# print(arr5)
# print(arr5[0][0][0])
# print(arr5[:2, :2])
# print(arr5[1, :2])

names = ['Bob', 'Jim', 'Chery', 'Bob', 'Sam']
namesarr = np.array(names)
# print(namesarr)
nums = np.array(np.random.randn(5, 4))
# print(nums)

namesB = namesarr == 'Bob'
# print(namesarr == 'Bob')
# print(nums[namesB])
# print((nums[~(namesB)]))
nums[nums < 0] = 0
# print(nums)

# 花式索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

# print(arr)
# print(arr[[2, 4, 0, 1]])

# arr = np.arange(32).reshape((8, 4))
# print(arr)
# print(arr[[2, 4, 6]][:,[0, 3, 1]])
# print(arr[np.ix_([1, 5, 7, 2], [1, 0, 2, 3])])

arr = np.arange(24).reshape((6, 4))
# print(arr)

# print(arr.T)
# print(np.transpose(arr))
# print(np.transpose(arr))
# print(np.dot(arr.T, arr))
# print(np.swapaxes(arr, 0, 1))
# print(arr)

# 一元函数
# print(np.sqrt(arr))
# print(np.exp(arr))

# 二元函数
arr11 = np.random.randn(5)
arr12 = np.random.randn(5)
# print(arr11)
# print(arr12)
# print(np.maximum(arr11, arr12))
# print(np.add(arr11, arr12))

arr = randn(5) * 5
# print(arr)
# print(np.modf(arr))
# print(np.isnan(arr))

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
# print(xs)
# print(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
# print(z)

# 三元表达式
arr13 = np.array([1.2, 2.3, 3.4, 4.5, 5.6, 6.7])
arr14 = np.array([12, 23, 34, 45, 56, 67])
arr15 = np.array([True, False, False, True, False, False])
arr16 = np.where(arr15, arr13, arr14)
# print(arr16)

arr17 = randn(5, 5)
# print(arr17)
# print(arr17.mean(axis=1))
# print(arr17.sum(axis=1))
# print(arr17.std(axis=1))

arr18 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.cumsum(arr18, axis=1))

arr = randn(100)
print((arr > 0).sum())

bools = np.array([True, False, True])
print(bools.any())
print(bools.all())




