import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/sales_2013.xlsx'
output_file = 'C:/Users/Administrator/Desktop/sales_2013_3.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
