import pandas as pd
import glob, os

input_file = 'C:/Users/Administrator/Desktop/'
output_file = 'C:/Users/Administrator/Desktop/sales_2013_12.xlsx'

all_workboks = glob.glob(os.path.join(input_file, '*.xls'))
data_frames = []
for workbook in all_workboks:
    all_workboks = pd.read_excel(workbook, sheet_name=None, index_col=True)
    for workbook_name, data in all_workboks.items():
        data_frames.append(data)

all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name="all_data_all_workbooks", index=False)
writer.save()
