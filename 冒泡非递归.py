from random import randint

def bubbleSort(lst, reverse=False):
    length = len(lst)
    for i in range(0, length):
        flag = False
        for j in range(0, length -i -1):
            exp='lst[j] > lst[j+1]'

            if reverse:
                exp = 'lst[j] < lst[j+1]'
            if eval(exp):
                lst[j],lst[j+1] = lst[j+1], lst[j]
                flag = True

        if not flag:
            break

lst = [randint(1,100) for i in range(20)]
print('Before sort:\n', lst)
bubbleSort(lst, True)
print('After sort:\n', lst)
