class tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def create_tree(root, val):
    # global backup
    newnode = tree()
    newnode.data = val
    newnode.left = None
    newnode.right = None
    if root == None:
        root = newnode
        return root
    else:
        current = root
        while current != None:

            backup = current
            if current.data > val:
                current = current.left
            else:
                current = current.right
        if backup.data > val:
            backup.left = newnode
        else:
            backup.right = newnode
    return root


def search(ptr, val):
    i = 1
    while True:
        if ptr == None:
            return None
        if ptr.data == val:
            print('共查找了 %3d 次' % i)
            return ptr
        elif ptr.data > val:
            ptr = ptr.left
        else:
            ptr = ptr.right
        i += 1


arr = [7, 1, 4, 2, 8, 13, 12, 11, 15, 9, 5]
ptr = None
print('[原始数组内容]')

for i in range(11):
    ptr = create_tree(ptr, arr[i])
    print('[%2d] ' % arr[i], end='')
print()
data = int(input('请输入查找值： '))
if search(ptr, data) != None:
    print('您想要找的值 [%3d] 找到了！！：' % data)
else:
    print('您要找的值没找到！')
