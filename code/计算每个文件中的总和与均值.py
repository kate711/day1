# 1 csv
import csv, glob, os, sys

input_path = 'C:/Users/Administrator/Desktop/b'
output_file = 'C:/Users/Administrator/Desktop/e.csv'

output_header_list = ['file_name', 'total_sales', 'average_sales']
csv_out_file = open(output_file, 'a', newline='')

filewriter = csv.writer(csv_out_file)
print(output_header_list)
filewriter.writerow(output_header_list)
for input_path in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_path, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_path))
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            number_of_sales += 1
            average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
            output_list.append(total_sales)
            output_list.append(average_sales)
        #   print(output_list)
        print(output_list)
        filewriter.writerow(output_list)
csv_out_file.close()

# 2 pandas
import pandas as pd
import glob, os, sys

input_path = 'C:/Users/Administrator/Desktop/b'
output_file = 'C:/Users/Administrator/Desktop/f.csv'

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)
    total_cost = pd.DataFrame(
        [float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).sum()
    average_cost = pd.DataFrame(
        [float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).mean()

    data = {'file_name': os.path.basename(input_file), 'total_sales': total_sales, 'average_sales': average_sales}

    all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales'], index=[0]))

data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)
