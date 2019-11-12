# 创建字典
empty_dict = {}
a_dict = {'one': 1, 'two': 2, 'three': 3}
print('{}'.format(a_dict))
print('a_dict has {!s} element'.format(len(a_dict)))

another_dict = {'x': 'printer', 'y': 5, 'z': ['star', 'circle', 9]}
print('{}'.format(another_dict))
print('a_dict has {!s} element'.format(len(a_dict)))

print('{}'.format(a_dict['two']))
print('{}'.format(another_dict['z']))

a_new_dict = a_dict.copy()
print('{}'.format(a_new_dict))

print('{}'.format(a_new_dict.keys()))
print('{}'.format(a_new_dict.values()))
print('{}'.format(a_new_dict.items()))
a_dict_keys = a_new_dict.keys()
print('{}'.format(a_dict_keys.items()))
