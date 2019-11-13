# 1  基础Python CSV
import csv
import re
import sys

input_file = 'C:/Users/Administrator/Desktop/supplier_data.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data1.csv'
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)  # ^ 表示搜索模式 001开头   .* 表示除换行符之外的任意字符
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                print(row_list)
                filewriter.writerow(row_list)

print('______________________')

# 2 pandas csv
import pandas as pd
import sys

input_file = 'C:/Users/Administrator/Desktop/supplier_data.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data2.csv'
data_frame = pd.read_csv(input_file)

data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]

print(data_frame_value_matches_pattern)
data_frame_value_matches_pattern.to_csv(output_file)
