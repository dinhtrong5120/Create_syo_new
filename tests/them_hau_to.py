import pandas as pd

# Dữ liệu mẫu
data = {
    'CADICS ID': ['A123', 'A123', 'B456', 'B456', 'C789', 'C789', 'A123'],
    'device_name': ['Device1', 'Device1', 'Device2', 'Device2', 'Device3', 'Device3', 'Device1'],
    'value': [10, 20, 30, 40, 50, 60, 70]
}

df = pd.DataFrame(data)

print("Dữ liệu ban đầu:")
print(df)
# Tạo một cột mới để đánh dấu các bản ghi trùng lặp
df['duplicate_count'] = df.groupby(['CADICS ID', 'device_name']).cumcount()

# Thêm hậu tố cho các bản ghi trùng lặp
df['CADICS ID'] = df.apply(lambda x: f"{x['CADICS ID']}_{x['duplicate_count']}" if x['duplicate_count'] > 0 else x['CADICS ID'], axis=1)

# Xóa cột duplicate_count
df = df.drop(columns=['duplicate_count'])

print("\nDữ liệu sau khi thêm hậu tố:")
print(df)