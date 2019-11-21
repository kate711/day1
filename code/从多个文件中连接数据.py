# 1 csv
import csv, glob, os, sys

input_path = 'C:/Users/Administrator/Desktop/b'
output_path = 'C:/Users/Administrator/Desktop/c.csv'

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_path, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader, None)
                for row in filereader:
                    filewriter.writerow(row)

# 2 使用pandas
import pandas as pd
import glob, os, sys

input_path = 'C:/Users/Administrator/Desktop/b'
output_path = 'C:/Users/Administrator/Desktop/d.csv'

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []
for file in all_files:
    data_frames = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frames)
data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
print(data_frames_concat)
data_frames_concat.to_csv(output_path, index=False)
