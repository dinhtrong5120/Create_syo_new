import os

import win32com.client
import pandas as pd
import re
import pythoncom


# Truong hop test thu ben duoi local
# def set_up(file_path):
#     pythoncom.CoInitialize()
#     # Extract the password from the file name
#     name = file_path.split('\\')
#     text = name[-1]
#     match = re.search(r'\((.*?)\)', text)
#     password_ = match.group(1)
#     # Initialize the Excel Application object
#     xlApp = win32com.client.Dispatch("Excel.Application")
#
#     # Open the Excel file and authenticate with the password
#     xlwb = xlApp.Workbooks.Open(file_path, False, True, None, password_)
#     sheet_name = 2
#     xlApp.Visible = False
#     xlwb.Worksheets(sheet_name).Activate()
#     sheet = xlwb.Worksheets(sheet_name)
#     return xlwb, xlApp, sheet
def set_up(file_path):
    pythoncom.CoInitialize()
    # Extract the password from the file name
    # name = file_path.split('\\')
    # text = name[-1]
    text = file_path
    match = re.search(r'\((.*?)\)', text)
    print('match: ', match)
    password_ = match.group(1)
    print('password_: ', password_)
    # Initialize the Excel Application object
    xlApp = win32com.client.Dispatch("Excel.Application")

    # Open the Excel file and authenticate with the password
    print("xxxxxxx")
    xlwb = xlApp.Workbooks.Open(file_path, False, True, None, password_)
    sheet_name = 2
    xlApp.Visible = False
    xlwb.Worksheets(sheet_name).Activate()
    sheet = xlwb.Worksheets(sheet_name)
    return xlwb, xlApp, sheet


def find_color_cell(sheet_, column_numbers_):
    gray_cells_ = []
    blue_cells_ = []
    delete_cells_ = [14]

    # Get the used range to determine the number of rows
    used_range = sheet_.UsedRange
    max_row = used_range.Rows.Count
    for column_number in column_numbers_:
        for row_idx in range(1, max_row + 1):
            cell = sheet_.Cells(row_idx, column_number)
            if column_number == 1:
                if cell.Interior.Color == int("535353", 16):  # Convert hex color to decimal
                    gray_cells_.append((cell.Value, cell.Row))
                    delete_cells_.append(cell.Row - 1)
                elif cell.Interior.Color == int("695224", 16):  # Convert hex color to decimal
                    blue_cells_.append((cell.Value, cell.Row))
                    delete_cells_.append(cell.Row - 1)
            elif cell.Interior.Color == 9868950.0 and cell.Row - 1 not in delete_cells_:
                delete_cells_.append(cell.Row - 1)
    return gray_cells_, blue_cells_, delete_cells_


def col_letter_to_num(letter):
    num = 0
    for char in letter:
        num = num * 26 + (ord(char.upper()) - ord('A')) + 1
    return num


def convert_address_to_indices(address):
    match = re.match(r"\$(\w+)\$(\d+):\$(\w+)\$(\d+)", address)
    if match:
        col_start_letter, row_start, col_end_letter, row_end = match.groups()
        col_start = col_letter_to_num(col_start_letter) - 1  # Zero-based index
        col_end = col_letter_to_num(col_end_letter) - 1  # Zero-based index
        row_start = int(row_start) - 1  # Zero-based index
        row_end = int(row_end) - 1  # Zero-based index
        return row_start, row_end, col_start, col_end
    else:
        raise ValueError("Invalid address format")


def find_merge(sheet_):
    # Initialize a list to store the merged areas
    merged_cells_list = []
    # Loop through each cell in the worksheet
    for row in range(1, sheet_.UsedRange.Rows.Count + 1):
        for column in range(1, sheet_.UsedRange.Columns.Count + 1):
            cell = sheet_.Cells(row, column)

            # Check if the cell is part of a merged area
            if cell.MergeCells:
                # Get the merged area
                merged_area = cell.MergeArea

                # Get the address of the merged area
                address = merged_area.Address

                # Append the address and value to the list
                if (address, cell.Value) not in merged_cells_list and cell.Value is not None:
                    merged_cells_list.append((address, cell.Value))
    # print(merged_cells_list)
    # Create a DataFrame from the unmerged sheet
    data = []
    for row in range(1, sheet_.UsedRange.Rows.Count + 1):
        row_data = []
        for column in range(1, sheet_.UsedRange.Columns.Count + 1):
            cell_value = sheet_.Cells(row, column).Value
            row_data.append(cell_value)
        data.append(row_data)

    df = pd.DataFrame(data)
    for address, value in merged_cells_list:
        row_start, row_end, col_start, col_end = convert_address_to_indices(address)
        for row in range(row_start, row_end + 1):
            for col in range(col_start, col_end + 1):
                df.iat[row, col] = value
    return df


def dataframe_convert(df_, gray_cells_list, blue_cells_list, delete_cells_list, project_name, xlwb, xlApp):
    project_name = project_name.upper()
    gray_cells_list = [('UNKNOW_device_group', 0)] + gray_cells_list + [('xxx', df_.shape[0])]
    blue_cells_list = [('UNKNOW_device', 0)] + blue_cells_list + [('xxx', df_.shape[0] + 1)]

    index_gray_old = 0
    value_gray_old = 'xxx'
    for item in gray_cells_list:
        if item[0] == 'UNKNOW_device_group':
            value_gray_old = item[0]  # UNKNOW_device_group
            index_gray_old = item[1]  # 0
        else:
            df_.loc[index_gray_old:item[1], 'device_group'] = value_gray_old  # [0:16]
            value_gray_old = item[0]
            index_gray_old = int(item[1])
    index_blue_old = 0
    value_blue_old = 'xxx'
    for item in blue_cells_list:
        if item[0] == 'UNKNOW_device':
            value_blue_old = item[0]
            index_blue_old = int(item[1])
        else:
            df_.loc[index_blue_old:int(item[1]), 'device_name'] = value_blue_old
            value_blue_old = item[0]
            index_blue_old = int(item[1])

    column_names = [i for i in range(1, df_.shape[1] + 1)]
    columns = [col for col in df_.columns if col not in ['device_group', 'device_name']]
    # columns.insert(0, 'project_name')
    columns.insert(0, 'device_group')
    columns.insert(1, 'device_name')
    df_ = df_[columns]

    df_.columns = column_names
    result = df_.stack()
    index_column_class = result[result == 'Class'].index[0][1]
    print()
    index_row_class = result[result == 'Class'].index[0][0]
    print("index_row_class: ", index_row_class)
    index_attributes = result[result == 'Attributes'].index[0][0]
    index_OptionPackage = result[result == 'Option Package'].index[0][0]
    index_row_zone = result[result == 'ZONE'].index[0][0]
    index_column_zone = result[result == 'ZONE'].index[0][1]
    print('index_column_zone: ', index_column_zone)
    df_end = df_.iloc[index_row_zone:, index_column_class:]

    df_end_region3 = df_end.loc[:index_row_class - 1, index_column_zone:]

    df_.drop(index=delete_cells_list, inplace=True)
    # Close the workbook and quit the application
    xlwb.Close(False)
    xlApp.Quit()

    return df_, df_end_region3, index_column_class, index_attributes, index_OptionPackage, index_row_zone, index_row_class, index_column_zone
    # return gray_cells_list, blue_cells_list


def main_process_spec(file_path, file_name):
    xlwb, xlApp, sheet = set_up(file_path)
    column_numbers = [1, 4, 6]
    gray_cells, blue_cells, delete_cells = find_color_cell(sheet, column_numbers)
    df = find_merge(sheet)

    df_, df_end_region3, index_column_class, index_attributes, index_OptionPackage, index_row_zone, index_row_class, index_column_zone = dataframe_convert(
        df, gray_cells, blue_cells, delete_cells, 'wz1j', xlwb, xlApp)
    return df_, df_end_region3
    # df_.to_excel('spec_wz1j_1.xlsx')
    # df_end_region3.to_excel('df_end_region3.xlsx')

# file_path = r"C:\Users\KNT21617\Downloads\newken\project\data\raw\(wz1j)WZ1J_Advanced_Spec_List_sq2 のコピー.xlsx"
# main(file_path)
