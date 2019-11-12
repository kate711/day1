from random import randint
def binarySearch(lst, start, end, value):

    if start > end :
        return False

    mid = (start + end ) // 2
    midValue = lst[mid]

    if midValue == value:
        return value
    elif midValue > value:
        return binarySearch(lst, start, mid - 1, value)
    else:
        return binarySearch(lst, mid + 1, end, value)

lst = [randint(1, 100) for i in range(200)]
lst.sort()
print(lst)
result = binarySearch(lst, 0, 100, 30)
if result :
    print('Success ,its position is: ', result)
else:
    print('Fail, Not exit.')