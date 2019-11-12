a_list = [1, 2, 3]
print('{}'.format(a_list))
print('{}'.format(len(a_list)))
print('{}'.format(max(a_list)))
print('{}'.format(min(a_list)))

b_list = ['print', 5, 5, ['star', 'circle', 9]]
print('{}'.format(b_list))
print('{}'.format(len(b_list)))
print('{}'.format(b_list.count(5)))

print('{}'.format(a_list[0]))
print('{}'.format(a_list[1]))
print('{}'.format(a_list[2]))
print('{}'.format(a_list[-1]))
print('{}'.format(a_list[-2]))
print('{}'.format(a_list[-3]))

print('{}'.format(a_list[0:2]))
print('{}'.format(a_list[:2]))
print('{}'.format(a_list[1:4]))
print('{}'.format(a_list[1:]))

# 列表复制
a_new_list = a_list[:]
print("{}".format(a_new_list))

# 列表连接
a_longer_list = a_list + a_new_list
print('{}'.format(a_longer_list))

a = 2 in a_list
print("{}".format(a))
if 2 in a_list:
    print('{}'.format(a_list))
b = 6 not in a_list
print('{}'.format(b))
if 6 not in a_list:
    print('{}'.format(a_list))

a_list.append(4)
a_list.append(5)
a_list.append(6)
print('{}'.format(a_list))
a_list.remove(5)
print('{}'.format(a_list))
a_list.pop()
a_list.pop()
print('{}'.format(a_list))

a_list.reverse()
print("{}".format(a_list))

unordered_list = [3, 5, 1, 7, 2, 5, 3, 4, 6, 6, 3, 8]
print('{}'.format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print('{}'.format(list_copy))
print('{}'.format(unordered_list))

my_lists = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 4, 1, 3]]
my_lists_sorted_by_index3 = sorted(my_lists, key=lambda index_value: index_value[3])
my_lists_sorted_by_index0 = sorted(my_lists, key=lambda index_value: index_value[0])
my_lists_sorted_by_index1 = sorted(my_lists, key=lambda index_value: index_value[1])
print('{}'.format(my_lists_sorted_by_index3))
print('{}'.format(my_lists_sorted_by_index0))
print('{}'.format(my_lists_sorted_by_index1))
