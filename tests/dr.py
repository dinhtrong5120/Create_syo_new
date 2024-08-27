import pandas as pd
import numpy as np


def process_dataframe(df):
    # Lọc các hàng hợp lệ
    valid_df = df[~df['group_key_map'].isin([None, '', 'default'])]
    # valid_df.to_excel(r"C:\Users\KNT21617\Downloads\output file\valid_df.xlsx")
    # Lấy danh sách các cột bắt đầu bằng 'conf-'
    conf_cols = [col for col in df.columns if col.startswith('conf-')]
    # print('conf_cols: ',conf_cols)
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
    result_df = pd.DataFrame(columns=df.columns)
    # print('result_df: ',result_df)
    # Áp dụng hàm trên từng group và lưu vào dataframe tạm thời
    for name, group in valid_df.groupby('group_key_map'):
        updated_group = update_conf_values(group.copy())  # Copy để tránh thay đổi original dataframe
        # print('updated_group: ', updated_group)
        result_df = pd.concat([result_df, updated_group])
        # print("result_df: ",result_df)
    # result_df.to_excel(r"C:\Users\KNT21617\Downloads\output file\result_df.xlsx")
    # Ghép các hàng không hợp lệ vào dataframe kết quả
    final_df = pd.concat([result_df, df[df['group_key_map'].isin([None, '', 'default'])]])
    print('final_df: ',final_df)
    final_df = final_df.sort_index()
    def update_conf_values(row):
        if row['default'] not in [None, np.nan, '']:
            for col in final_df.columns:
                if col.startswith('conf-'):
                    final_df.at[row.name, col] = row['default']

    # Áp dụng hàm update_conf_values cho từng hàng
    final_df.apply(update_conf_values, axis=1)
    return final_df


def update_conf_columns(df):
    def update_conf_values(row):
        if row['default'] not in [None, np.nan, '']:
            for col in df.columns:
                if col.startswith('conf-'):
                    df.at[row.name, col] = row['default']

    # Áp dụng hàm update_conf_values cho từng hàng
    df.apply(update_conf_values, axis=1)

    return df


if __name__ == '__main__':
    # Example usage:
    data = {
        'group_key_map': ['A', 'B', 'A', 'default', 'default', 'B'],
        'conf-1': ['value1', 'value2', 'value1', 'value3', 'value4', 'value2'],
        'conf-2': ['x', 'value6', 'value500000000', 'value7', 'value8', 'value7'],
        'other-1': [10, 20, 30, 40, 50, 60],
        'other-2': [100, 200, 300, 400, 500, 600],
        'default': ['A', None, 'B', '', 'C', 'D']
    }

    df = pd.DataFrame(data)
    print('Original dataframe:')
    print(df)

    final_df = process_dataframe(df)
    print('\nProcessed dataframe:')
    print(final_df)

    updated_df = update_conf_columns(final_df)
    print("updated_df: ", updated_df)
