class tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


# 中序遍历
def inorder(ptr):
    if ptr != None:
        inorder(ptr.left)
        print('[%2d] ' % ptr.data, end='')
        inorder(ptr.right)


# 后序遍历
def postorder(ptr):
    if ptr != None:
        inorder(ptr.left)
        inorder(ptr.right)
        print('[%2d] ' % ptr.data, end='')


# 前序遍历
def preorder(ptr):
    if ptr is not None:
        print('[%2d] ' % ptr.data, end='')
        inorder(ptr.left)
        inorder(ptr.right)


# 链表建立二叉树
def create_tree(root, val):
    global backup
    newnode = tree()
    newnode.data = val
    newnode.left = None
    newnode.right = None

    if root is None:
        root = newnode
        return root
    else:
        current = root
        while current is not None:
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


# 主程序
data = [5, 6, 24, 8, 12, 3, 17, 1, 9]
ptr = None
root = None

for i in range(9):
    ptr = create_tree(ptr, data[i])
print('=========================')
print('排序完成的结果：')
inorder(ptr)  # 中序遍历
print('')
postorder(ptr)
print('')
preorder(ptr)
print('')
