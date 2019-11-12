import sys

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book2.csv'

# 1
with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str, header_list)) + '\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str, row_list)) + '\n')

print('-----------------------')

# 2 使用CSV模块
import csv, sys

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book4.csv'

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)

# 3 行中值满足某个条件
import csv, sys

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book5.csv'

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0]).strip()
            cost = str(row_list[3]).strip("$").replace(',', '')
            if supplier == 'Supplier Z' or float(cost) > 600.0:
                filewriter.writerow(row_list)

# print('行中的值属于某个集合')
import csv, sys

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book7.csv'

important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)
