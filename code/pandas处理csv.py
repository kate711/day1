# 1 读写
import sys
import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book3.csv'
data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)

# 2 筛选特定的行

import sys
import pandas as pd

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book6.csv'
data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

data_frame_value_meets_condition = data_frame.loc[
                                   (data_frame['Supplier Name'].str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)

# 3 行中的值属于某个集合
import pandas as pd
import sys

input_file = 'C:/Users/Administrator/Desktop/Book1.csv'
output_file = 'C:/Users/Administrator/Desktop/Book8.csv'

data_frame = pd.read_csv(input_file)
important_dates = ['1/20/14', '1/30/14']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]
data_frame_value_in_set.to_csv(output_file, index=False)
