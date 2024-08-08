# # import pandas as pd
# #
# #
# # def logic_add(df_):
# #     list_key_row_index = []
# #     list_conf_column = []
# #     list_comment_value = []
# #     list_comment_column = []
# #     list_led_row_index = []
# #     result_dict = {}
# #     levelizer_index = 0
# #     list_key_levelizer = ['AUTO LEVELIZER', 'MANUAL LEVELIZER', 'HEAD LAMP LEVELIZER']
# #     for item in list_key_levelizer:
# #         key_rows = df_.loc[df_['CADICS ID'] == item].index
# #         if not key_rows.empty:
# #             key_row = key_rows[0]
# #             list_key_row_index.append((item, key_row))
# #             if item == 'HEAD LAMP LEVELIZER':
# #                 levelizer_index = key_row
# #     if 'FRONT LIGHT' in df['CADICS ID'].values:
# #         index_row_frontlight = df_.loc[df_['CADICS ID'] == 'FRONT LIGHT'].index[0]
# #         for col in df_.columns:
# #             if col.startswith('conf-'):
# #                 list_conf_column.append(col)
# #                 value = df.loc[index_row_frontlight, col]
# #                 if value not in result_dict:
# #                     result_dict[value] = []
# #                 result_dict[value].append(col)
# #                 # list_key_value.append((col, value))
# #             if col.startswith('comment'):
# #                 value_1 = df.loc[index_row_frontlight, col]
# #                 if pd.notna(value_1):
# #                     list_comment_value.append(value_1)
# #                 list_comment_column.append(col)
# #             df.loc[levelizer_index, list_comment_column] = df.loc[index_row_frontlight, list_comment_column]
# #     # print('result_dict: ', result_dict)
# #     # print('list_key_row_index: ', list_key_row_index)
# #     for item_1, list_col in result_dict.items():
# #         # print('item_1: ', item_1)
# #         # print('list_col: ', list_col)
# #         for item_2 in list_comment_value:
# #             if item_1 in item_2:
# #                 for item_3 in list_key_row_index:
# #                     if item_3[0] in item_2:
# #                         df.loc[item_3[1], list_col] = 'w'
# #                         list_col_ = list(set(list_conf_column) - set(list_col))
# #                         df.loc[item_3[1], list_col_] = '-'
# #                         if levelizer_index != 0:
# #                             df.loc[levelizer_index, list_col_] = item_3[0]
# #
# #     list_key_led = ['LED LB', 'HALOGEN HEADLAMP', 'HEADLAMP TYPE']
# #     led_lb_index = 0
# #     for item in list_key_led:
# #         led_rows = df_.loc[df_['CADICS ID'] == item].index
# #         if not led_rows.empty:
# #             key_row = led_rows[0]
# #             print("item: ", item)
# #             print('key_row: ', key_row)
# #             list_led_row_index.append((item, key_row))
# #             if item == 'LED LB':
# #                 led_lb_index = key_row
# #     for column in list_conf_column:
# #         if df.at[led_lb_index, column] == 'w':
# #             for item in list_led_row_index:
# #                 if item[0] == 'HALOGEN HEADLAMP':
# #                     df.at[item[1], column] = 'w/o'
# #                 if item[0] == 'HEADLAMP TYPE':
# #                     df.at[item[1], column] = 'LED'
# #         elif df.at[led_lb_index, column] == 'w/o':
# #             for item in list_led_row_index:
# #                 if item[0] == 'HALOGEN HEADLAMP':
# #                     df.at[item[1], column] = 'w'
# #                 if item[0] == 'HEADLAMP TYPE':
# #                     df.at[item[1], column] = '-'
# #     return df
#
import pandas as pd


def logic_add(df):
    list_key_row_index = []
    list_conf_column = [col for col in df.columns if col.startswith('conf-')]
    list_comment_column = [col for col in df.columns if col.startswith('comment')]
    result_dict = {}
    levelizer_index = 0
    list_key_levelizer = ['AUTO LEVELIZER', 'MANUAL LEVELIZER', 'HEAD LAMP LEVELIZER']

    # Tìm các hàng có chứa các từ khóa trong list_key_levelizer
    for item in list_key_levelizer:
        key_rows = df.loc[df['CADICS ID'] == item].index
        if not key_rows.empty:
            key_row = key_rows[0]
            list_key_row_index.append((item, key_row))
            if item == 'HEAD LAMP LEVELIZER':
                levelizer_index = key_row

    # Kiểm tra và xử lý giá trị 'FRONT LIGHT'
    if 'FRONT LIGHT' in df['CADICS ID'].values:
        index_row_frontlight = df.loc[df['CADICS ID'] == 'FRONT LIGHT'].index[0]
        for col in list_conf_column:
            value = df.at[index_row_frontlight, col]
            result_dict.setdefault(value, []).append(col)
        for col in list_comment_column:
            df.at[levelizer_index, col] = df.at[index_row_frontlight, col]

    for item_1, list_col in result_dict.items():
        for item_2 in df.loc[index_row_frontlight, list_comment_column]:
            if isinstance(item_2, str) and item_1 in item_2:
                for item_3 in list_key_row_index:
                    if item_3[0] in item_2:
                        df.loc[item_3[1], list_col] = 'w'
                        list_col_ = list(set(list_conf_column) - set(list_col))
                        df.loc[item_3[1], list_col_] = '-'
                        if levelizer_index != 0:
                            df.loc[levelizer_index, list_col_] = item_3[0]

    list_key_led = ['LED LB', 'HALOGEN HEADLAMP', 'HEADLAMP TYPE']
    led_lb_index = df.loc[df['CADICS ID'] == 'LED LB'].index[0] if not df.loc[
        df['CADICS ID'] == 'LED LB'].index.empty else 0

    for column in list_conf_column:
        if df.at[led_lb_index, column] == 'w':
            df.loc[df['CADICS ID'] == 'HALOGEN HEADLAMP', column] = 'w/o'
            df.loc[df['CADICS ID'] == 'HEADLAMP TYPE', column] = 'LED'
        elif df.at[led_lb_index, column] == 'w/o':
            df.loc[df['CADICS ID'] == 'HALOGEN HEADLAMP', column] = 'w'
            df.loc[df['CADICS ID'] == 'HEADLAMP TYPE', column] = '-'

    return df


if __name__ == '__main__':
    path_file = r"C:\Users\KNT21617\Downloads\output file\仕様表_WZ1L.xlsx"
    df = pd.read_excel(path_file)
    # result = logic_add(df)
    df_end = logic_add(df)
    df_end.to_excel(r"C:\Users\KNT21617\Downloads\output file\仕様表_WZ1L_lol.xlsx")
    # print('result: ', result)

# import pandas as pd
# import numpy as np
#
# # Tạo dataframe ví dụ
# data = {
#     'group_key': ['A', 'B', 'A', 'default', 'default', 'B'],
#     'conf-1': ['value1', 'value2', 'value1', 'value3', 'value4', 'value2'],
#     'conf-2': ['x', 'value6', 'value500000000', 'value7', 'value8', 'value7'],
#     'other-1': [10, 20, 30, 40, 50, 60],
#     'other-2': [100, 200, 300, 400, 500, 600],
#     'value': ['A', None, 'B', '', 'C', 'D']
# }
#
# df = pd.DataFrame(data)
# print('data: ', df)
# # Lọc các hàng hợp lệ
# valid_df = df[~df['group_key'].isin([None, '', 'default'])]
#
# # Lấy danh sách các cột bắt đầu bằng 'conf-'
# conf_cols = [col for col in df.columns if col.startswith('conf-')]
#
#
# # Tạo hàm để chỉnh sửa các giá trị 'conf-'
# def update_conf_values(group):
#     for col in conf_cols:
#         unique_values = group[col].unique()
#         # Lấy giá trị đầu tiên không phải là '-'
#         valid_value = next((val for val in unique_values if val != '-'), None)
#         if valid_value:
#             group[col] = valid_value
#     return group
#
#
# # Áp dụng hàm trên từng group
# updated_df = valid_df.groupby('group_key').apply(update_conf_values)
#
# # Ghép các hàng không hợp lệ vào dataframe mới
# final_df = pd.concat([updated_df, df[df['group_key'].isin([None, '', 'default'])]])
#
# print(final_df)
import pandas as pd
import numpy as np


def process_dataframe(df):
    # Lọc các hàng hợp lệ
    valid_df = df[~df['group_key'].isin([None, '', 'default'])]

    # Lấy danh sách các cột bắt đầu bằng 'conf-'
    conf_cols = [col for col in df.columns if col.startswith('conf-')]

    # Tạo hàm để chỉnh sửa các giá trị 'conf-'
    def update_conf_values(group):
        for col in conf_cols:
            unique_values = group[col].unique()
            # Lấy giá trị đầu tiên không phải là '-'
            valid_value = next((val for val in unique_values if val != '-'), None)
            if valid_value:
                group[col] = valid_value
        return group

    # Áp dụng hàm trên từng group
    updated_df = valid_df.groupby('group_key').apply(update_conf_values)

    # Ghép các hàng không hợp lệ vào dataframe mới
    final_df = pd.concat([updated_df, df[df['group_key'].isin([None, '', 'default'])]])

    return final_df


def update_conf_columns(df):
    def update_conf_values(row):
        if row['value'] not in [None, np.nan, '']:
            for col in df.columns:
                if col.startswith('conf-'):
                    df.at[row.name, col] = row['value']

    # Áp dụng hàm update_conf_values cho từng hàng
    df.apply(update_conf_values, axis=1)

    return df


if __name__ == '__main__':
    # Example usage:
    data = {
        'group_key': ['A', 'B', 'A', 'default', 'default', 'B'],
        'conf-1': ['value1', 'value2', 'value1', 'value3', 'value4', 'value2'],
        'conf-2': ['-', 'value6', 'value500000000', 'value7', 'value8', 'value7'],
        'other-1': [10, 20, 30, 40, 50, 60],
        'other-2': [100, 200, 300, 400, 500, 600],
        'value': ['A', None, 'B', '', 'C', 'D']
    }

    df = pd.DataFrame(data)
    print('Original dataframe:')
    print(df)

    final_df = process_dataframe(df)
    print('\nProcessed dataframe:')
    print(final_df)

    updated_df = update_conf_columns(final_df)
    print("updated_df: ", updated_df)

#
#
# # Example usage:
# data = {
#     'value': ['A', None, 'B', '', 'C'],
#     'conf-1': [1, 2, 3, 4, 5],
#     'conf-2': [6, 7, 8, 9, 10],
#     'conf-3': [11, 12, 13, 14, 15]
# }
#
# df = pd.DataFrame(data)
# updated_df = update_conf_columns(df)
# print(updated_df)
