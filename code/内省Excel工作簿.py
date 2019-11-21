from xlrd import open_workbook

input_file = r'C:\Users\Administrator\Desktop\sales_2013.xlsx'

workbook = open_workbook(input_file)
print('Number of worksheet : ', workbook.nsheets)
for worksheet in workbook.sheets():
    print('Worksheet name: ', worksheet.name, '\tRows:', worksheet.nrows, \
          '\tColums:', worksheet.ncols)
