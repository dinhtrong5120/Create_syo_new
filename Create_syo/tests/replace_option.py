import pandas as pd

def replace_values_in_dataframe(df, list_tuples):
    for tuple_item in list_tuples:
        search_value = tuple_item[0]
        replace_value = tuple_item[1]

        df.loc[df['CADICS ID'] == search_value, 'CADICS ID'] = replace_value

    return df

# Tạo DataFrame mẫu
data = {'CADICS ID': ['A123', 'B456', 'C789', 'D012', 'E345'],
        'Value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# List các tuple
list_tuples = [('A123', 'NewValue1'), ('C789', 'NewValue2'), ('E345', 'NewValue3')]

# Gọi hàm replace_values_in_dataframe và in ra kết quả
result_df = replace_values_in_dataframe(df, list_tuples)
print(result_df)