import math
def Cni1(n, i):
    return int(math.factorial(n) / math.factorial(i)/math.factorial(n - i))
x = Cni1(800, 7)

print(x)

