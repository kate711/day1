from random import random
def payGames(number):
    T0 = random()
    for k,v in number.items():
        if v[0] <= T0 < v[1]:
            return k

    number = {'one':(0,0.08),
              'two':(0.08,0.3),
              'three':(0.3,1.0)}

get  = dict()
本次战况 = 0
for i in range(1000):
    get[本次战况] = get.get(本次战况,0) + 1

for item in get.items():
        print(item)