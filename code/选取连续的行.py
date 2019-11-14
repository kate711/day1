# 1 csv
import csv
import sys

input_file = 'C:/Users/Administrator/Desktop/supplier_data_unnecessary_header_footer.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data_unnecessary_header_footer1.csv'
row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                print([value.strip() for value in row])
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1

print('---------------------------------')

# 使用pandas
import pandas as pd
import sys

input_file = 'C:/Users/Administrator/Desktop/supplier_data_unnecessary_header_footer.csv'
output_file = 'C:/Users/Administrator/Desktop/supplier_data_unnecessary_header_footer2.csv'
data_frame = pd.read_csv(input_file, header=None)
# 根据行索引丢弃列
data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
# 选取一行作为列索引
data_frame.columns = data_frame.iloc[0]
# 为数据框重新生成索引,删除多余的索引
data_frame = data_frame.reindex(data_frame.index.drop([3]))
print(data_frame)
data_frame.to_csv(output_file, index=False)
