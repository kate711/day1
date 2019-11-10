# 创建元组
my_tuple = ('x', 'y', 'z')
print('{}'.format(my_tuple))
print('{}'.format(len(my_tuple)))
print('{}'.format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print('{}'.format(longer_tuple))

# 元组解包
one, two, three = my_tuple
print('{0} {1} {2}'.format(one, two, three))
var1 = 'red'
var2 = 'robin'
print('{} {}'.format(var1, var2))
var1, var2 = var2, var1
print('{} {}'.format(var1, var2))

# 元组转成列表
my_list = [1, 2, 3, 4]
my_tuple = ('x', 'y', 'z')
print('{}'.format(tuple(my_list)))
print('{}'.format(list(my_tuple)))
