import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/sales_2013.xlsx'
output_file = 'C:/Users/Administrator/Desktop/sales_2013_11.xlsx'

my_sheets = [0, 1]
threshold = 1900.0
data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)
row_list = []
for worksheet_name, data in data_frame.items():
    row_list.append(data[data['Sale Amount'].astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='666666666666666', index=False)
writer.save()
