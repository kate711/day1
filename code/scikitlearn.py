"""
# 决策树
# 输入数据
# X 对应的类别
# 创建模型
# 训练模型
# 测试数据，分类结果
# 测试数据，分类结果的概率
"""

from sklearn import tree

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf.predict([[2., 2.]]))
print(clf.predict_proba([[2., 2.]]))
