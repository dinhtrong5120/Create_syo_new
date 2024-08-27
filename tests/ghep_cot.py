# import pandas as pd
#
# # Tạo một DataFrame mẫu
# data = {
#     'CADICS ID': ['A123', 'B456', 'A123', 'C789', 'B456', 'D012', 'D012', 'E345'],
#     'Product Name': ['Product 1', 'Product 2', 'Product 1', 'Product 3', 'Product 2', 'Product 4', 'Product 4', 'Product 5'],
#     'Price': [100, 200, 100, 300, 200, 400, 400, 500]
# }
#
# valid_df = pd.DataFrame(data)
#
# # Hiển thị DataFrame
# print("DataFrame ban đầu:")
# print(valid_df)
#
# # Sử dụng câu lệnh để tìm các giá trị trùng lặp trong cột 'CADICS ID'
# duplicated_elements_ = valid_df[valid_df.duplicated('CADICS ID', keep=False)]['CADICS ID'].unique().tolist()
#
# # Hiển thị kết quả
# print("\nCác CADICS ID trùng lặp:")
# print(duplicated_elements_)

import pandas as pd

# Tạo một DataFrame mẫu
data = {
    'CADICS ID': ['A123', 'B456', 'A123', 'C789', 'B456', 'D012', 'D012', 'E345', 'A123'],
    'Product Name': ['Product 1', 'Product 2', 'Product 1', 'Product 3', 'Product 2', 'Product 4', 'Product 4',
                     'Product 5', 'Product 6'],
    'Price': [100, 200, 100, 300, 200, 400, 400, 500, 600]
}

valid_df = pd.DataFrame(data)

# Hiển thị DataFrame ban đầu
print("DataFrame ban đầu:")
print(valid_df)

# Tạo một từ điển để theo dõi số lần xuất hiện
counts = {}


# Hàm để thêm hậu tố cho các giá trị trùng lặp
def add_suffix(cadics_id):
    if cadics_id in counts:
        counts[cadics_id] += 1
        return f"{cadics_id}_{counts[cadics_id]}"
    else:
        counts[cadics_id] = 0  # Đặt giá trị ban đầu là 0 (lần đầu tiên không có hậu tố)
        return cadics_id  # Trả về giá trị gốc cho lần xuất hiện đầu tiên


# Áp dụng hàm cho cột 'CADICS ID'
valid_df['CADICS ID'] = valid_df['CADICS ID'].apply(add_suffix)

# Hiển thị DataFrame mới
print("\nDataFrame sau khi thêm hậu tố:")
print(valid_df)
