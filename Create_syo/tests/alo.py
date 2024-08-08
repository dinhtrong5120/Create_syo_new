import pandas as pd
from sqlalchemy import create_engine

# Tạo engine kết nối đến cơ sở dữ liệu
str_connect = "mysql+mysqlconnector://" + 'root' + ":" + 'SQL123456' + "@" + 'localhost' + "/" + 'db_new_prj_final'
engine = create_engine(str_connect)
df = pd.read_sql_table('device_details',
                       columns=['device_name', 'auto_detail', 'group_detail', 'option_detail', 'device_details_name',
                                'group_key_map', 'default'], con=engine)
df_1 = pd.read_sql_table('device', columns=['device_group', 'device_name'], con=engine)

# print(df)
# print(df_1)
# df.to_excel('device_details.xlsx')
merged_df_1 = pd.merge(df_1, df, on='device_name', how='inner')
merged_df_1_2 = merged_df_1.sort_values(['device_group','device_name'])
print(merged_df_1_2)
# merged_df_1_2.to_excel('merged_df_1_2.xlsx')
