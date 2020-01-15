def Btree_create(btree, data, length):
    for i in range(1, length):
        level = 1
        while btree[level] != 0:
            if data[i] > btree[level]:
                level = level * 2 + 1
            else:
                level = level * 2
        btree[level] = data[i]


length = 9
data = [0, 6, 3, 5, 4, 7, 8, 9, 2]
btree = [0] * 16
print('原始数组内容')

for i in range(length):
    print('[%2d]' % data[i], end='')
print('')

Btree_create(btree, data, 9)
print('二叉树内容')
for i in range(1, 16):
    print('[%2d]' % btree[i], end='')
