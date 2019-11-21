from xlrd import open_workbook
from xlwt import Workbook
#
# input_file = 'C:/Users/Administrator/Desktop/sales_2013.xlsx'
# output_file = 'C:/Users/Administrator/Desktop/sales_2013_1.xlsx'

# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('jan_2013_output')
#
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     for row_index in range(worksheet.nrows):
#         for column_index in range(worksheet.ncols):
#             print(row_index,column_index)
#             output_worksheet.write(row_index, column_index, \
#                                    worksheet.cell_value(row_index, column_index))
#             output_workbook.save(output_file)


# 2 pandas
import pandas as pd
import sys

input_file = 'C:/Users/Administrator/Desktop/sales_2013.xlsx'
output_file = 'C:/Users/Administrator/Desktop/sales_2013_2.xlsx'

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
