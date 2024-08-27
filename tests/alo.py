import pandas as pd
from sqlalchemy import create_engine

# Tạo engine kết nối đến cơ sở dữ liệu
str_connect = "mysql+mysqlconnector://" + 'root' + ":" + 'SQL123456' + "@" + 'localhost' + "/" + 'db_new_prj_final'
engine = create_engine(str_connect)
# df = pd.read_sql_table('device_details',
#                        columns=['device_name', 'auto_detail', 'group_detail', 'option_detail', 'device_details_name',
#                                 'group_key_map', 'default'], con=engine)
# df_1 = pd.read_sql_table('device', columns=['device_group', 'device_name'], con=engine)
# list_sap_xep = ['UNKNOW_device', 'LIGHTING', 'GLASSES', 'SIDE VIEW MIRROR / CAMERA', 'REAR VIEW MIRROR / CAMERA',
#                 'COMBI METER', 'HMI',
#                 'PHYSICAL SWITCHES', 'STEERING', 'PEDALS AND FOOT-REST', 'GEAR SHIFT', 'PARKING BRAKE',
#                 'WINDOW OPENING', 'SUN VISOR', 'DRIVER SEAT', 'ASSIST SEAT', '2ND ROW SEAT', 'HEADREST', 'TRIM',
#                 '1ST ROW STORAGE', '2ND ROW STORAGE', 'TRUNK / LUGGAGE STORAGE', 'FUNCTIONAL LIGHTING',
#                 'AMBIENT LIGHTING', 'PASSENGER SUPPORT', 'INNER PROTECTION', 'CARPETS', 'TYPE OF INTERIOR DECORATION',
#                 'AMENITY', 'AIR CONDITIONING AND HEATING', 'AIR QUALITY MANAGEMENT', 'AUDIO & NAVIGATION', 'SPEAKERS',
#                 'SOUND BUBBLE', 'NVH MANAGEMENT', 'ACCESS', 'OPENING', 'PROTECTION', 'ACCESSORY', 'LOGO & EMBLEM',
#                 'SUSPENSION', 'BRAKING', 'DRIVING MODE', 'ECO DRIVING AIDS', 'TIRES', 'WHEELS & WHEEL COVERS',
#                 'SPARE WHEEL', 'ADAS COMFORT', 'ADAS SAFETY', 'ADAS PARKING', 'WARNING & ALERT', 'AIRBAGS', 'SEAT BELT',
#                 'OTHER', 'SPECIFICATION', 'CHARGER', 'PLUG / CABLE', 'EV DEDICATED FEATURES']
# # print(df)
# # print(df_1)
# # df.to_excel('device_details.xlsx')
# # merged_df_1 = pd.merge(df_1, df, on='device_name', how='inner')
# # # merged_df_1_2 = merged_df_1.sort_values(['device_group', 'device_name'])
# # # merged_df_1_2 = merged_df_1.sort_values(by='device_name', key=lambda x: x.map({v: i for i, v in enumerate(list_sap_xep)}))
# # # Sửa lỗi AttributeError: 'str' object has no attribute 'map'
# # # Sort the DataFrame
# # merged_df_1_2 = merged_df_1.sort_values(
# #     by=['device_group'],
# #     key=lambda x: (x['device_name'].map({v: i for i, v in enumerate(list_sap_xep)}))
# # )
# # print(merged_df_1_2)
# # merged_df_1_2.to_excel('merged_df_1_2.xlsx')
# # Merge DataFrames
# merged_df_1 = pd.merge(df_1, df, on='device_name', how='inner')
#
# # Tạo cột ánh xạ thứ tự cho `device_name`
# merged_df_1['device_name_order'] = merged_df_1['device_name'].apply(
#     lambda x: list_sap_xep.index(x) if x in list_sap_xep else len(list_sap_xep))
#
# # Sắp xếp theo `device_group` và sau đó theo thứ tự của `device_name`
# merged_df_1_2 = merged_df_1.sort_values(by=['device_group', 'device_name_order', 'group_key_map'])
#
#
# # Xóa cột tạm thời `device_name_order`
# merged_df_1_2 = merged_df_1_2.drop(columns=['device_name_order'])
#
# # In và lưu kết quả
# print(merged_df_1_2)
# merged_df_1_2.to_excel('merged_df_1_2_sorted_xxx.xlsx', index=False)
df = pd.read_sql_table('value_inf',
                       columns=['project_id','config_id','parameter_name','value'], con=engine)
print(df)