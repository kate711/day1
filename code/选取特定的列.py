# 1 使用列索引值
import csv, sys

input_file = 'C:/Users/Administrator/Desktop/supplier_data.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data3.csv'
my_columns = [0, 3]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            print(row_list_output)
            filewriter.writerow(row_list_output)

print('-----------------')
# 1 pandas
import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/supplier_data.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data4.csv'

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
print(data_frame_column_by_index)
data_frame_column_by_index.to_csv(output_file, index=False)

print('--------------------------------')

# 2 使用列标题
import csv
import sys

input_file = 'C:/Users/Administrator/Desktop/supplier_data.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data5.csv'

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader, None)

        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
                print(my_columns_index)
                print(my_columns)
        filewriter.writerow(my_columns)

        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
                print(row_list_output)
            filewriter.writerow(row_list_output)

print('-----------------------------------')

# 2 pandas
import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/supplier_data.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data6.csv'

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
print(data_frame_column_by_name)
data_frame_column_by_name.to_csv(output_file, index=False)
