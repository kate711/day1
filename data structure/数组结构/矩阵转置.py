arrA = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
N = 4
# 声明 4X4 数组arr
arrB = [[None] * N for row in range(N)]
print('[原设置的矩阵内容]')
# for i in range(4):
#     for j in range(4):
#         print('%d' %arrA[i][j],end='\t')
for i in arrA:
    print(i)

# 进行矩阵转置的操作
for i in range(4):
    for j in range(4):
        arrB[i][j] = arrA[j][i]

print('转置后的矩阵为：')

for i in arrB:
    print(i)

print('--------------------')

# numpy

import numpy as np

# a = np.array([(1,2,3), (4,5,6)])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(a, '\n')

b = a.transpose()
print(b)
