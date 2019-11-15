import csv
import glob
import os
import sys

# path = "C:/Users/Administrator/Desktop/c"
# os.mkdir(path)
input_path = 'C:/Users/Administrator/Desktop/b'
file_counter = 0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader, None)
        for row in filereader:
            row_counter += 1
            print('{0!s}: \t{1:d} rows \t{2:d} colums'.format(os.path.basename(input_path), row_counter, len(header)))
            file_counter += 1
        print('Number of files: {0:d}'.format(file_counter))
