# 1
A = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
N = 3
C = [[None] * N for row in range(N)]

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]
print('[矩阵A和矩阵B相加的结果]')
# for i in range(3):
#     for j in range(3):
#         # print('%d' %C[i][j],end='\t')
for k in C:
    print(k)

print('---------------------------------')

# 2
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# 迭代输出行
for i in range(len(X)):
    # 迭代输出列
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)
