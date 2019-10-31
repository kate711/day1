import random
def mergeSort(seq,reverse=False):
    # 把表拆成两部分
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]

    if len(left) > 1:
        left = mergeSort(left)
    if len(right) > 1:
        right = mergeSort(right)

    temp = []
    while left and right :
        if left[-1] >=  right[-1]:
            temp.append(left.pop())
        else:
            temp.append(right.pop())
    temp.reverse()

    result = (left or right) + temp

    # 逆序
    if reverse:
        i,j = 0,len(result) -1
        while i < j:
            result[i],result[j]= result[j],result[i]
            i += 1
            j -= 1
    return result

for i in range(10000):
    reverse = random.choice((True, False))
    x = [random.randint(1,100) for i in range(20)]
    print(x)
    y = sorted(x, reverse = reverse)
    x =mergeSort(x,reverse)
    if x != y:
        print('error')

    print(x)
