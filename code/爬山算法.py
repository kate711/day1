from random import randint,random
def hillMax(lst,howFar):
    """
    爬山算法
    :param lst: 待确定最大值的列表
    :param howFar: 看得越远越准确
    :return:
    """
    assert howFar>1, 'howFar must > 1'

    start = 0
    ll = len(lst)
    while start <= ll:
        m = lst[start]
        loc = lst[start+1:start+howFar]
        mm = max(loc)
        if m > mm:
            return m
        else:
            mmPos = loc.index(mm)
            start += mmPos + 1

def simAnnealingMax(lst,howFar):
    """
    模拟退火算法
    :param lst:
    :param howFar:
    :return:
    """
    assert howFar>1,'parameter "howFar" must > 1'
    start = 0
    ll = len(lst)

    times = 1
    while start <= ll:
        m = lst[start]
        loc = lst[start+1:start+howFar]

        if not loc:
            return m

        mm = max(loc)
        mmPos = loc.index(mm)

        if m <= mm:
            start += mmPos+1
        else:
            delta = (m-mm)/(m+mm)
            if delta <= random()/times:
                start += mmPos+1
                times += 1
            else:
                return m

for j in range(10):
    win = 0
    compareTimes = 1000
    for i in range(compareTimes):
        lst = [randint(1,100) for i in range(200)]
        k = 3
        if simAnnealingMax(lst,k) >= hillMax(lst,k):
            win += 1

    if win >= compareTimes//2:
        print('win')

