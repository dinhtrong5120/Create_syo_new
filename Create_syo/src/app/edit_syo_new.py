import pandas as pd
import numpy as np


def logic_add(df):
    list_key_row_index = []
    list_conf_column = [col for col in df.columns if str(col).startswith('conf-')]
    list_comment_column = [col for col in df.columns if str(col).startswith('comment') or isinstance(col, int)]
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


def process_dataframe(df_):
    df_['default'] = df_['default'].fillna('')
    # Lọc các hàng hợp lệ
    valid_df = df_[~df_['group_key_map'].isin([None, '', 'default_key', np.nan])]
    if not valid_df.empty:
        valid_df.to_excel(r"C:\Users\KNT21617\Downloads\output file\valid_df.xlsx")
        # Lấy danh sách các cột bắt đầu bằng 'conf-'
        conf_cols = [col for col in df_.columns if str(col).startswith('conf-')]

        # Tạo hàm để chỉnh sửa các giá trị 'conf-'
        def update_conf_values(group):
            for col in conf_cols:
                unique_values = group[col].unique()
                # Lấy giá trị đầu tiên không phải là '-'
                valid_value = next((val for val in unique_values if val != '-'), None)
                if valid_value:
                    group[col] = valid_value
            return group

        # Tạo một dataframe tạm thời để lưu kết quả
        result_df = pd.DataFrame(columns=df_.columns)
        # Áp dụng hàm trên từng group và lưu vào dataframe tạm thời
        for name, group in valid_df.groupby('group_key_map'):
            updated_group = update_conf_values(group.copy())  # Copy để tránh thay đổi original dataframe
            result_df = pd.concat([result_df, updated_group])

        # Ghép các hàng không hợp lệ vào dataframe kết quả
        final_df = pd.concat([result_df, df_[df_['group_key_map'].isin([None, '', 'default_key', np.nan])]])
        final_df = final_df.sort_index()

        def update_conf_values(row):
            if row['default'] not in [None, np.nan, '']:
                for col in final_df.columns:
                    if str(col).startswith('conf-'):
                        final_df.at[row.name, col] = row['default']

        # Áp dụng hàm update_conf_values cho từng hàng
        final_df.apply(update_conf_values, axis=1)
        return final_df
    else:
        def update_conf_values(row):
            if row['default'] not in [None, np.nan, '', np.NaN]:
                print(row['default'])
                print('okkkk')
                for col in df_.columns:
                    if str(col).startswith('conf-'):
                        df_.at[row.name, col] = row['default']

        # Áp dụng hàm update_conf_values cho từng hàng
        df_.apply(update_conf_values, axis=1)
        return df_

#
# if __name__ == '__main__':
#     path_file = r"C:\Users\KNT21617\Downloads\output file\仕様表_WZ1L.xlsx"
#     df = pd.read_excel(path_file)
#     # result = logic_add(df)
#     df_1 = logic_add(df)
#     print(df_1)
#     df_2 = process_dataframe(df_1)
#     df_2.to_excel(r"C:\Users\KNT21617\Downloads\output file\仕様表_WZ1L_lol_3.xlsx")
#     print('result: ', df_2)
