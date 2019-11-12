from math import log


def calcshang(dataSet):
    lenDataSet = len(dataSet)
    p = {}
    H = 0.0
    for data in dataSet:
        currentLabel = data[-1]  # 获取类别标签
        if currentLabel not in p.keys():  # 若字典中不存在该类别标签，即创建
            p[currentLabel] = 0
        p[currentLabel] += 1  # 递增类别标签的值
    for key in p:
        px = float(p[key] / float(lenDataSet))  # 计算某个标签的概率
        H -= px * log(px, 2)  # 计算信息熵
    return H


dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
print(calcshang(dataSet))
