from collections import defaultdict

def yanghui(n):
    triangle = defaultdict(int)
    for row in range(n):
        # 每行第一个元素为1
        triangle[row, 0] = 1
        print(triangle[row, 0], end='\t')
        # 生成该行后续元素
        for col in range(1, row+1):
            triangle[row, col] = triangle[row-1, col-1] + triangle[row-1, col]
            print(triangle[row, col], end= '\t')
        print()

yanghui(10)
