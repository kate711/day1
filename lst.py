from itertools import combinations
from random import sample

def subAscendingList(lst):
    ''' 返回最长子序列'''
    for length in range(len(lst), 0, -1):
        for sub in combinations(lst, length):
            if list(sub) == sorted(sub):
                return sub

def getList(start = 0, end = 1000, number = 20):
    """生成随机序列"""
    if number > end - start:
        return None
    return sample(range(start,end), number)

def main():
    lst = getList(number=10)
    if lst is not None:
        print(lst)
        print(subAscendingList(lst))

main()