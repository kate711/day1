# 1 csv
import csv

input_file = 'C:/Users/Administrator/Desktop/supplier_data_no_header_row.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data_no_header_row1.csv'

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
        print(header_list)
        filewriter.writerow(header_list)
        for row in filereader:
            print(row)
            filewriter.writerow(row)

print('---------------------------')

# 2 pandas
import pandas as pd
import sys

input_file = 'C:/Users/Administrator/Desktop/supplier_data_no_header_row.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data_no_header_row2.csv'
header_list = ['Supplier Name', 'Invoice Nunmber', 'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
print(data_frame)
data_frame.to_csv(output_file, index=False)
