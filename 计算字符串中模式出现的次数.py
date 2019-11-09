from math import exp, log, sqrt
import re

string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
pattern1 = re.compile(r"(?P<match_word>The)", re.I)  # </match_word>
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("output: {0:d}".format(count))

# 找到时打印出来
for word in string_list:
    if pattern1.search(word):
        print("{:s}".format(pattern1.search(word).group('match_word')))

# 查找并替换
string_to_find = r'The'
pattern2 = re.compile(string_to_find, re.I)
print('output:{:s}'.format(pattern2.sub("a", string)))
