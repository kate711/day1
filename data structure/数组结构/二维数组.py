N = 2
arr = [[None] * N for row in range(N)]
print('|a1 a2|')
print('|a2 b2|')
arr[0][0] = input('请输入a1:')
arr[0][1] = input('请输入b1:')
arr[1][0] = input('请输入a2:')
arr[1][1] = input('请输入b2:')
# 二阶行列式
result = int(arr[0][0]) * int(arr[1][1]) - int(arr[0][1]) * int(arr[1][0])
print('|%d %d|' % (int(arr[0][0]), int(arr[0][1])))
print('|%d %d|' % (int(arr[1][0]), int(arr[1][1])))
print('行列式的值=%d' % result)
