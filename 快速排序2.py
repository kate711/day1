from random import randint

# 更改最大递归深度
import sys
sys.setrecursionlimit(100000000)

def quickSort(x, start, end):
    if start >= end:
        return

    i = start
    j = end

    # 使用第一个元素作为枢点
    key = x[start]

    while i < j:
        # 从后向前寻找第一个比指定元素小的元素
        while i < j and x[j] >= key:
            j -= 1
        x[i] = x[j]

        # 从前向后寻找第一个比指定元素大的元素
        while i < j and x[i] <= key:
            i += 1
        x[j] = x[i]

    x[i] = key
    quickSort(x, start, i - 1)
    quickSort(x, i + 1, end)
x = [randint(1, 1000) for i in range(1000000)]
print(x)
quickSort(x,start=0, end=len(x)-1)
print(x)


