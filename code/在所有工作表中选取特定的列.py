import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/sales_2013.xlsx'
output_file = 'C:/Users/Administrator/Desktop/sales_2013_9.xlsx'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
column_output = []
for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='666', index=False)
writer.save()
