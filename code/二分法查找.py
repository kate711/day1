def binarySearch(lst, value):
    start = 0
    end = len(lst)
    while start < end:
        middle = (start + end) // 2   # +, -, *, /, //, **, ~, %分别表示加法或者取正、减法或者取负、乘法、除法、整除、乘方、取补、取余
        if value == lst[middle]:
            return middle
        elif value > lst[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return False


from random import randint

lst = [randint(1, 50) for i in range(20)]
lst.sort()
print(lst)
x = int(input('输入要查找的整数：'))
result = binarySearch(lst, x)
if result:
    print('Success , its postion is :', result)
else:
    print('Fail ' + str(x) + ' Not exit.')
