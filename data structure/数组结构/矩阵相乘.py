# out(i,j)=a(i,k)b(k,j)
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])
print(np.dot(a, b))
print(np.matmul(a, b))
print(a.dot(b))

print('---------------------')

# # out(i,j)=a(i,j)b(i,j)
print(np.multiply(a, a))

print('---------------------')
# 普通矩阵相乘

print(np.mat(a) * np.mat(b))
