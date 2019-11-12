import sys
import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book3.csv'
data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)
