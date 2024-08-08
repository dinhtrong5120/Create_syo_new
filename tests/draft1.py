# import pandas as pd
# # Tạo một DataFrame mẫu
# data = {
#     'Name': ['A', 'A', 'A', 'A'],
#     'Subject': [1, 1, 2, 3],
#     'Score': [101, 102, 103, 104]
# }
# df = pd.DataFrame(data)
# print(df)
# print("ahihi")
# # Biến đổi DataFrame từ dạng dọc thành dạng rộng
# # pivot_df = df.pivot(index='Name', columns='Subject', values='Score')
# pivot_df = df.pivot(columns='Subject', values='Score')
#
# # In ra DataFrame biến đổi
# print(pivot_df)
# pivot_table = df.pivot_table(values='Score', columns='Subject', aggfunc='mean')
# print('**********************')
# print('pivot_table: ',pivot_table)


# import pandas as pd
#
# # Tạo một DataFrame mẫu
# data = {
#     'Name': ['A', 'B', 'A', 'A'],
#     'Subject': [1, 1, 2, 3],
#     'Score': [101, 102, 103, 104]
# }
# df = pd.DataFrame(data)
#
# # Thêm một cột chỉ số nhóm
# # df['group_index'] = [0, 1, 0, 0]
#
# # # Biến đổi DataFrame từ dạng dọc thành dạng rộng
# # pivot_df = df.pivot(index='Name', columns='Subject', values='Score')
# #
# # # In ra DataFrame biến đổi
# # print(pivot_df)
# df['count'] = None
# # df_ref = df.copy()
# a1 = 0
# temp = 0
# for index, row in df.iterrows():
#     print(index)
#     if index == 0:
#         a1 = row['Subject']
#         row['count'] = 1
#         temp = 1
#         continue
#     a2 = row['Subject']
#     if a2 == a1:
#         row['count'] = temp + 1
#     else:
#         a1 = row['Subject']
# print(df)
# import pandas as pd
#
# # Tạo một DataFrame mẫu
# data = {
#     'Name': ['A', 'B', 'A', 'A'],
#     'Subject': [1, 1, 2, 3],
#     'Score': [101, 102, 103, 104]
# }
# df = pd.DataFrame(data)
#
# # Thêm một cột chỉ số nhóm
# df['count'] = 0
#
# # Sử dụng loc để cập nhật giá trị trong DataFrame
# a1 = 0
# temp = 0
# for index, row in df.iterrows():
#     if index == 0:
#         a1 = row['Subject']
#         df.loc[index, 'count'] = 1
#         temp = 1
#         continue
#     a2 = row['Subject']
#     if a2 == a1:
#         temp += 1
#         df.loc[index, 'count'] = temp
#     else:
#         a1 = row['Subject']
#         temp = 1
#         df.loc[index, 'count'] = temp
#
# print(df)
# pivot_df = df.pivot(index='count', columns='Subject', values='Score')
# print(pivot_df)


import pandas as pd

# Tạo một DataFrame mẫu
data = {
    'Name': ['A', 'A', 'A', 'A'],
    'Subject': [1, 1, 2, 3],
    'Score': [101, 102, 103, 104]
}
df = pd.DataFrame(data)

# Tạo cột 'count' bằng cách sử dụng groupby và cumcount
df['count'] = df.groupby('Subject').cumcount() + 1

# Biến đổi DataFrame từ dạng dọc thành dạng rộng
pivot_df = df.pivot(index=['count', 'Name'], columns='Subject', values='Score')

# In ra DataFrame biến đổi
print("Original DataFrame:")
print(df)
print("\nPivot DataFrame:")
print(pivot_df.reset_index())

# Lấy danh sách các giá trị Subject từ pivot_df
value_vars = [col for col in pivot_df.columns if col not in ['count', 'Name']]

# Biến đổi ngược lại từ pivot_df sang df
unpivot_df = pivot_df.reset_index().melt(id_vars=['count', 'Name'], value_vars=value_vars,
                                         var_name='Subject', value_name='Score').dropna()

# Đổi kiểu dữ liệu của cột 'Subject' thành int
unpivot_df['Subject'] = unpivot_df['Subject'].astype(int)

# Sắp xếp DataFrame theo cột 'Subject'
unpivot_df = unpivot_df.sort_values(by=['Subject'])

# In ra DataFrame đã biến đổi ngược lại
print("\nUnpivoted DataFrame:")
print(unpivot_df.reset_index(drop=True))