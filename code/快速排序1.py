from random import randint


def quickSort(lst, reverse=False):
    if len(lst) <= 1:
        return lst

    # 默认使用最后一个元素作为枢点
    pivot = lst.pop()
    first, second = [], []

    # 默认升序排列，True降序排列
    if reverse == False:
        exp = 'x <= pivot'

    if reverse == True:
        exp = 'x >= pivot'

    for x in lst:
        first.append(x) if eval(exp) else second.append(x)
    #        if eval(exp):
    #            first.append(x)
    #        else:
    #            second.append(x)

    return quickSort(first, reverse) + [pivot] + quickSort(second, reverse)


lst = [randint(1, 1000) for i in range(10)]
print(quickSort(lst, True))
