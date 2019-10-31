import random
def kp(arr,i,j):
    if i < j:
        base = kpgc(arr,i,j)
        kp(arr,i,base)
        kp(arr,base+1,j)

def kpgc(arr,i,j):
    base = arr[i]
    while i < j:
        while i < j and arr[j] > base:
            j -= 1
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
        arr[i] = base
    return i
lst = [random.randint(0,1000) for i in range(10)]
print(lst)
kp(lst,0,len(lst)-1)
print(lst)